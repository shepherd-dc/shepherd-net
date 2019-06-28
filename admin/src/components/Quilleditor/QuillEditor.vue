<template>
  <quill-editor
    ref="myQuillEditor"
    v-model="content"
    :options="editorOption"
    @blur="onEditorBlur($event)"
    @focus="onEditorFocus($event)"
    @change="onEditorChange($event)"/>
</template>

<script>
import { quillEditor } from 'vue-quill-editor'
import hljs from 'highlight.js' // 语法高亮
// import 'highlight.js/styles/xcode.css'
import 'highlight.js/styles/monokai-sublime.css'
export default {
  components: {
    quillEditor
  },
  data() {
    return {
      content: '<p>I am Example</p>',
      editorOption: {
        // some quill options
        modules: {
          toolbar: [
            ['bold', 'italic', 'underline', 'strike'],
            ['blockquote', 'code-block'],
            [{ 'header': 1 }, { 'header': 2 }], // custom button values
            [{ 'script': 'sub' }, { 'script': 'super' }], // superscript/subscript
            [{ 'list': 'ordered' }, { 'list': 'bullet' }],
            [{ 'indent': '-1' }, { 'indent': '+1' }], // outdent/indent
            [{ 'direction': 'rtl' }] // text direction

            // [{ 'size': ['small', false, 'large', 'huge'] }],  // custom dropdown
            // [{ 'header': [1, 2, 3, 4, 5, 6, false] }],

            // [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
            // [{ 'font': [] }],
            // [{ 'align': [] }],

            // ['clean']                                         // remove formatting button
          ],
          syntax: {
            highlight: text => hljs.highlightAuto(text).value // 语法高亮插件调用
          }
        }
      }
    }
  },
  mounted() {
    // console.log('app init, my quill insrance object is:', this.myQuillEditor)
    setTimeout(() => {
      this.content = 'i am changed'
    }, 3000)
  },
  methods: {
    onEditorBlur(editor) {
      // console.log('editor blur!', editor)
    },
    onEditorFocus(editor) {
      // console.log('editor focus!', editor)
    },
    onEditorReady(editor) {
      // console.log('editor ready!', editor)
    },
    onEditorChange({ quill, html, text }) {
      // console.log('editor change!', quill, html, text)
      this.content = html
      this.$emit('deliverContent', html)
    }
  }
}
</script>

<style lang="scss">
  .ql-editor {
    min-height: 500px;
    overflow-y: auto;
  }
  .ql-toolbar.ql-snow {
    padding: 0 0 0 8px!important;
    border-radius: 4px 4px 0 0;
  }
  .ql-container.ql-snow {
    border-radius: 0 0 4px 4px;
  }
</style>
