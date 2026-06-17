# HM_RECOMMENDATION_EXT

> This table stores all the information related to a recommendation provided by an external source.

**Description:** Health Maintenance Recommendation External  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DUE_DT_TM` | DATETIME |  |  | Date when the external recommendation is due |
| 4 | `DUE_IND` | DOUBLE | NOT NULL |  | Indicates whether the source is due or not |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `EXTERNAL_NAME` | VARCHAR(255) |  |  | Displayable name of the external source |
| 7 | `FREQUENCY_TEXT` | VARCHAR(255) |  |  | The frequency between when the external source should be recommended |
| 8 | `LAST_SATISFACTION_DT_TM` | DATETIME |  |  | Date when this source was last satisfied |
| 9 | `OUTCOME_TEXT` | VARCHAR(255) |  |  | The outcome of the external source |
| 10 | `RECOMMENDATION_EXT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 11 | `RECOMMENDATION_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the recommendation to which the external info belongs |
| 12 | `SOURCE_TEXT_IDENT` | VARCHAR(500) |  |  | The character identifier of the external source |
| 13 | `SOURCE_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of external source. 1 = travel immunization, 2 = Healthe Registry Measure |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `VALUE_TEXT` | VARCHAR(255) |  |  | The value and/or unit to display for the source |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RECOMMENDATION_ID` | [HM_RECOMMENDATION](HM_RECOMMENDATION.md) | `RECOMMENDATION_ID` |

