---
title: Vue Quick Start
keywords:
  - Vue
  - Code
  - Developer
  - Front-end
description: ""
created: 2025-05-04 13:49:24
updated: 2025-05-04 13:49:24
---

[Vue - Get Started](https://vuejs.org/guide/introduction.html)

## Reactivity

[Reactivity Fundamentals](https://vuejs.org/guide/essentials/reactivity-fundamentals.html)

```vue
<template>
  <strong>{{ timegoUrl }}</strong>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const timegoUrl = ref('https://timego.app')

console.log(timegoUrl) // { value: https://timego.app }
console.log(timegoUrl.value) // { https://timego.app }
</script>
```

Notice that we did not need to append `.value` when using the ref in the template.

[Why Refs?](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#why-refs)

## Rendering

### Conditional Rendering v-if and v-show

[Conditional Rendering](https://vuejs.org/guide/essentials/conditional.html)

#### v-if

```vue
<template>
  <h1 v-if="isTimegoUrl">https://timego.app</h1>
</template>
<script setup lang="ts">
const isTimegoUrl = ref(true)
</script>
```

```vue
<template>
  <h1 v-if="urlType === 'timego'">https://timego.app</h1>
</template>
<script setup lang="ts">
import { ref } from 'vue'
const urlType = ref('')
</script>
```

#### v-if and v-else

```vue
<template>
  <h1 v-if="isTimegoUrl">https://timego.app</h1>
  <h1 v-else>Oh no 😢 https://chrisding.xyz/</h1>
</template>
<script setup lang="ts">
import { ref } from 'vue'
const isTimegoUrl = ref(true)
</script>
```

#### v-else-if

```vue
<template>
  <h1 v-if="urlType ==== 'chris'">https://chrisding.xyz/about</h1>
  <h1 v-else-if="urlType ==== 'txtify'">https://txtify.app</h1>
  <h1 v-else-if="urlType ==== 'timego'">https://timego.app</h1>
  <h1 v-else-if="urlType ==== '1024'">https://1024.dev</h1>
  <h1 v-else>Oh no 😢</h1>
</template>
<script setup lang="ts">
import { ref } from 'vue'
const urlType = ref('')
</script>
```

#### v-show

```vue
<template>
  <h1 v-show="timegoUrl">{{ timegoUrl }}</h1>
</template>
<script setup lang="ts">
import { ref } from 'vue'
const timegoUrl = ref('https://timego.app')
</script>
```

Nots: v-show doesn't support the `<template>` element, nor does it work with `v-else`.

### List Rendering v-for

[Vue - List Rendering](https://vuejs.org/guide/essentials/list.html)

```vue
<template>
  <h1>Time Partner - timego.app</h1>
  <ul>
    <li v-for="(item, index) in items" :key=index>
      {{ item.name }} : {{ item.url }}
    </li>
  </ul>
</template>
<script setup lang="ts">
import { ref } from 'vue'
const items = ref([{ name: 'Timego - Home', url: 'https://timego.app' }, { name: 'Timego - Calendar', url: 'https://timego.app/calendar' }])
</script>
```

Result:

```html
<h1>Time Partner - timego.app</h1>
<ul>
  <li>Timego - Home : https://timego.app</li>
  <li>Timego - Calendar : https://timego.app/calendar</li>
</ul>
```

### Nots

- It's not recommended to use v-if and v-for on the same element due to implicit precedence. Refer to [list rendering guide](https://vuejs.org/guide/essentials/list.html#v-for-with-v-if) for details.

## Computed Properties

[Computed Properties](https://vuejs.org/guide/essentials/computed.html)

```vue
<template>
  <input v-model="search"/>
  <ul>
    <li v-for="(item, index) in filteredItems" :key=index>
      {{ item.name }} : {{ item.url }}
    </li>
  </ul>
</template>
<script setup lang="ts">
import { ref, computed } from 'vue'
const search = ref('')
const items = [
  { name: 'Timego - Home', url: 'https://timego.app'},
  { name: 'Timego - Calendar', url: 'https://timego.app/calendar'},
]

const filteredItems = computed(() =>
  search.value === ''
    ? items
    : items.filter((item) => {
      return item.name.toLowerCase().includes(search.value.toLowerCase())
    })
)
</script>
```

## Watchers

[Watchers](https://vuejs.org/guide/essentials/watchers.html)

```vue
<script setup lang="ts">
import { ref, watch } from 'vue'

const x = ref(0)

watch(x, (newX) => {
  console.log(`new x is ${newX}`)
})
</script>
```

```vue
<script setup lang="ts">
import { ref, watch } from 'vue'

const x = ref(0)

watch(x, (newX, oldX) => {
  console.log(newx, oldX)
})
</script>
```

```vue
<script setup lang="ts">
import { ref, watch } from 'vue'

const x = ref(0)
const y = ref(0)

watch(
  [x, y],
  ([newX, newY]) => {
    //...
  },
)
</script>
```

`watch` is lazy by default: the callback won't be called until the watched source has changed. But in some cases we may want the same callback logic to be run eagerly - for example, we may want to fetch some initial data, and then re-fetch the data whenever relevant state changes.

We can force a watcher's callback to be executed immediately by passing the immediate: true option:

```vue
<script setup lang="ts">
import { ref, watch } from 'vue'

const source = ref('')

watch(
  source,
  (newValue, oldValue) => {
    // executed immediately, then again when `source` changes
  },
  { immediate: true }
)
</script>
```
