from dash import html, dcc

# Color scheme matching main app
COLORS = {
    'primary': '#6366f1',
    'primary_dark': '#4f46e5',
    'secondary': '#8b5cf6',
    'background': '#0f172a',
    'surface': '#1e293b',
    'text': '#f1f5f9',
    'text_secondary': '#94a3b8'
}

layout = html.Div([
    # Header Section
    html.Div([
        html.Div([
            dcc.Link("← Back", href='/', style={
                'color': COLORS['text_secondary'],
                'textDecoration': 'none',
                'fontSize': '1rem',
                'fontWeight': '500',
                'transition': 'color 0.3s ease',
                'display': 'inline-block',
                'marginBottom': '2rem'
            }),
            html.H1("BG", style={
                'fontSize': '3rem',
                'fontWeight': '700',
                'background': f'linear-gradient(135deg, {COLORS["primary"]} 0%, {COLORS["secondary"]} 100%)',
                'WebkitBackgroundClip': 'text',
                'WebkitTextFillColor': 'transparent',
                'marginBottom': '0.5rem',
                'letterSpacing': '-0.02em'
            }),
            html.P("Business Graphics Dashboard", style={
                'fontSize': '1.25rem',
                'color': COLORS['text_secondary'],
                'marginBottom': '3rem'
            })
        ], style={
            'maxWidth': '1200px',
            'margin': '0 auto',
            'padding': '3rem 2rem'
        })
    ]),
    
    # Content Section
    html.Div([
        html.Div([
            # Placeholder content cards
            html.Div([
                html.H3("Analytics", style={
                    'fontSize': '1.5rem',
                    'fontWeight': '600',
                    'marginBottom': '1rem',
                    'color': COLORS['text']
                }),
                html.P("Your business analytics content goes here.", style={
                    'color': COLORS['text_secondary'],
                    'lineHeight': '1.6'
                })
            ], style={
                'background': COLORS['surface'],
                'padding': '2rem',
                'borderRadius': '1rem',
                'border': f'1px solid rgba(99, 102, 241, 0.2)',
                'marginBottom': '1.5rem'
            }),
            
            html.Div([
                html.H3("Reports", style={
                    'fontSize': '1.5rem',
                    'fontWeight': '600',
                    'marginBottom': '1rem',
                    'color': COLORS['text']
                }),
                html.P("Generate and view business reports.", style={
                    'color': COLORS['text_secondary'],
                    'lineHeight': '1.6'
                })
            ], style={
                'background': COLORS['surface'],
                'padding': '2rem',
                'borderRadius': '1rem',
                'border': f'1px solid rgba(99, 102, 241, 0.2)',
                'marginBottom': '1.5rem'
            }),
            
            html.Div([
                html.H3("Visualizations", style={
                    'fontSize': '1.5rem',
                    'fontWeight': '600',
                    'marginBottom': '1rem',
                    'color': COLORS['text']
                }),
                html.P("Interactive business data visualizations.", style={
                    'color': COLORS['text_secondary'],
                    'lineHeight': '1.6'
                })
            ], style={
                'background': COLORS['surface'],
                'padding': '2rem',
                'borderRadius': '1rem',
                'border': f'1px solid rgba(99, 102, 241, 0.2)'
            })
        ], style={
            'maxWidth': '1200px',
            'margin': '0 auto',
            'padding': '0 2rem 3rem 2rem'
        })
    ])
], style={
    'minHeight': '100vh',
    'background': f'linear-gradient(135deg, {COLORS["background"]} 0%, #1a2332 100%)',
    'color': COLORS['text'],
    'fontFamily': '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
})