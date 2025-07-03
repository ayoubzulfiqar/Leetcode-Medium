import pandas as pd

def article_views_ii(views: pd.DataFrame) -> pd.DataFrame:
    grouped_views = views.groupby(['viewer_id', 'view_date'])['article_id'].nunique().reset_index()
    multi_article_views = grouped_views[grouped_views['article_id'] > 1]
    result_viewer_ids = multi_article_views['viewer_id'].unique()
    result_df = pd.DataFrame({'viewer_id': result_viewer_ids})
    result_df = result_df.sort_values(by='viewer_id').reset_index(drop=True)
    return result_df