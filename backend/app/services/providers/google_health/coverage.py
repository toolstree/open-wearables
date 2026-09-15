from app.schemas.enums import SeriesType
from app.services.providers.apple.coverage import HEALTH_SCORES, SLEEP_FIELDS, WORKOUT_FIELDS
from app.services.providers.google_health.metrics import METRICS

# Series from the unified rollUp + list metric registry.
TIMESERIES: frozenset[SeriesType] = frozenset(s for m in METRICS for s in m.series_types())

__all__ = ["HEALTH_SCORES", "SLEEP_FIELDS", "TIMESERIES", "WORKOUT_FIELDS"]
