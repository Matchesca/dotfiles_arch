return {
	'nvim-treesitter/nvim-treesitter',
	build = ":TSUpdate",
	opts = {
		-- A list of parser names, or "all" (the listed parsers MUST always be installed)
		ensure_installed = {
			"bash",
			"c",
			"cpp",
			"css",
			"go",
			"html",
			"javascript",
			"json",
			"lua", -- Essential for Neovim config
			"markdown",
			"markdown_inline", -- Required for markdown rendering
			"python",
			"query", -- Required for Treesitter queries, including highlighting
			"rust",
			"typescript",
			"vim", -- Essential for Neovim config/scripts
			"vimdoc", -- Essential for Neovim help files
			"yaml",
		},

		-- Install parsers synchronously (only applied to `ensure_installed`)
		sync_install = false,

		-- Automatically install missing parsers when entering buffer
		-- Recommendation: set to false if you don't have `tree-sitter` CLI installed locally
		auto_install = true,

		highlight = {
			enable = true,

			-- Setting this to true will run `:h syntax` and tree-sitter at the same time.
			-- Set this to `true` if you depend on 'syntax' being enabled (like for indentation).
			-- Using this option may slow down your editor, and you may see some duplicate highlights.
			-- Instead of true it can also be a list of languages
			additional_vim_regex_highlighting = false,
		},

		-- Enable indentation based on Treesitter
		indent = {
			enable = true,
			-- can disable indentation for specific languages if needed
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

	},
	config = function(_,opts)
		require("nvim-treesitter.configs").setup(opts)
	end,
}
