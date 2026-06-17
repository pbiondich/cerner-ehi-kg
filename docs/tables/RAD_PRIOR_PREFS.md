# RAD_PRIOR_PREFS

> Stores the number of relevant priors to retrieve and the look-back range per modality as specified by a user.

**Description:** RadNet Prior Preferences  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | Stores the code value for the activity sub-type that is used to filter order catalog items within activity type. Radiology modality. |
| 2 | `LOOKBACK_RANGE_UOM_CD` | DOUBLE | NOT NULL |  | The measure of the date range in lookback_range_value. |
| 3 | `LOOKBACK_RANGE_VALUE` | DOUBLE | NOT NULL |  | Date range for relevant priors to qualify. A value of zero denotes that the entire history should be considered. |
| 4 | `PRIOR_DISPLAY_QTY` | DOUBLE | NOT NULL |  | Maximum number of relevant priors to display. |
| 5 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that these preferences are set for. |
| 6 | `RAD_PRIOR_PREFS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RAD_PRIOR_PREFS table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

