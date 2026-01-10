return {
    'MunifTanjim/prettier.nvim',
    event = {'BufReadPre', 'BufNewFile'},
    config = function()
      require("prettier").setup({
        bin = 'prettier',
        filetypes = {
          "css", "graphql", "html", "javascript", "javascriptreact",
          "json", "less", "markdown", "scss", "typescript",
          "typescriptreact", "yaml",
        },
      })
      -- This gives you the :Prettier command without LSP
      vim.keymap.set('n', '<Leader>f', '<Plug>(prettier-format)', {})
    end
}
