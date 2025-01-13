from pathlib import Path
import shutil
import yaml
import markdown
import frontmatter
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

class MarkdownSite:
    def __init__(self, config_path: str = "config.yaml"):
        self.config = self._load_config(config_path)
        self.setup_jinja()
        self.setup_markdown()

    def _load_config(self, config_path: str) -> dict:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def setup_jinja(self):
        self.jinja_env = Environment(
            loader=FileSystemLoader('templates'),
            autoescape=True
        )

    def setup_markdown(self):
        self.md = markdown.Markdown(extensions=[
            'fenced_code',
            'tables'
        ])

    def process_markdown_file(self, file_path: Path) -> dict:
        post = frontmatter.load(str(file_path))
        html_content = self.md.convert(post.content)

        # 生成 URL 安全的标题
        safe_title = post.metadata.get('slug') or self.slugify(post.metadata.get('title', 'untitled'))

        return {
            'content': html_content,
            'title': post.metadata.get('title', 'Untitled'),
            'created': post.metadata.get('created', ''),
            'updated': post.metadata.get('updated', ''),
            'url': f"/posts/{safe_title}",
            'file_path': f"/posts/{safe_title}.html"  # 实际文件路径带 .html
        }

    def slugify(self, text: str) -> str:
        """将标题转换为 URL 安全的格式"""
        # 这是一个简单的实现，您可以根据需要扩展
        return text.lower().replace(' ', '-')

    def copy_static_files(self):
        static_dir = Path(self.config['paths']['static'])
        output_dir = Path(self.config['paths']['output'])

        if static_dir.exists():
            static_output = output_dir / 'static'
            if static_output.exists():
                shutil.rmtree(static_output)
            shutil.copytree(static_dir, static_output)

    def generate_site(self):
        content_dir = Path(self.config['paths']['content'])
        output_dir = Path(self.config['paths']['output'])

        # 清理并创建输出目录
        if output_dir.exists():
            shutil.rmtree(output_dir)
        output_dir.mkdir(parents=True)

        # 创建 posts 目录
        posts_dir = output_dir / 'posts'
        posts_dir.mkdir(exist_ok=True)

        # 处理所有文章
        posts = []
        for md_file in content_dir.rglob("*.md"):
            # 处理文章
            post_data = self.process_markdown_file(md_file)
            posts.append(post_data)

            # 渲染文章页面
            template = self.jinja_env.get_template('post.html')
            html = template.render(
                site={
                    **self.config['site'],
                    'year': datetime.now().year,
                    'author': self.config['site'].get('author', '')
                },
                post=post_data
            )

            # 保存文章
            output_file = output_dir / post_data['file_path'].lstrip('/')
            output_file.parent.mkdir(exist_ok=True)
            output_file.write_text(html, encoding='utf-8')

        # 生成索引页
        self.generate_index(posts, output_dir)

        # 生成 about 页面
        self.generate_about(output_dir)

        # 复制静态文件
        self.copy_static_files()

        print(f"成功生成网站！共处理 {len(posts)} 篇文章")

    def generate_index(self, posts: list, output_dir: Path):
        template = self.jinja_env.get_template('index.html')
        html = template.render(
            site={
                **self.config['site'],
                'year': datetime.now().year,
                'author': self.config['site'].get('author', '')
            },
            posts=sorted(posts, key=lambda x: x['updated'] or '', reverse=True)
        )

        output_file = output_dir / 'index.html'
        output_file.write_text(html, encoding='utf-8')

    def generate_about(self, output_dir: Path):
        """生成 about 页面"""
        template = self.jinja_env.get_template('about.html')
        html = template.render(
            site={
                **self.config['site'],
                'year': datetime.now().year,
                'author': self.config['site'].get('author', '')
            },
            projects=self.config.get('projects', [])
        )

        output_file = output_dir / 'about.html'
        output_file.write_text(html, encoding='utf-8')

if __name__ == '__main__':
    site = MarkdownSite()
    site.generate_site()
