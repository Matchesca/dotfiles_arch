require'nvim-treesitter.configs'.setup {
  -- A list of parser names, or "all" (the listed parsers MUST always be installed)
  ensure_installed = { "javascript", "typescript", "python", "c", "lua", "vim", "vimdoc", "query", "markdown", "markdown_inline", "go" },

  -- Install parsers synchronously (only applied to `ensure_installed`)
  sync_install = false,

  -- Automatically install missing parsers when entering buffer
  -- Recommendation: set to false if you don't have `tree-sitter` CLI installed locally
  auto_install = true,

  ---- If you need to change the installation directory of the parsers (see -> Advanced Setup)
  -- parser_install_dir = "/some/path/to/store/parsers", -- Remember to run vim.opt.runtimepath:append("/some/path/to/store/parsers")!

  highlight = {
    enable = true,

  },

  incremental_selection = {
    enable = true,
    keymaps = {
      -- Start selection with 'v' key (same as regular visual mode)
      init_selection = "<CR>",  -- Starts selection from the cursor

      -- Move to the next level of selection
      node_incremental = "<Tab>",  -- Select next text object (word, line, function, etc.)
      node_decremental = "<S-Tab>", -- Select previous text object

    },
  },
}
