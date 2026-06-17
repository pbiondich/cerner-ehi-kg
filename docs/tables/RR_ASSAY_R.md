# RR_ASSAY_R

> Stores the assay(s) defined for a round robin template

**Description:** Round Robin Assay Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DISPLAY_SEQUENCE` | DOUBLE |  |  | Defines the discrete task assay display sequence order as defined in the Round Robin Build application. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `OUTLIER` | DOUBLE |  |  | Defines the value defined in Round Robin Build to designate the outlier value. |
| 6 | `OUTLIER_IND` | DOUBLE |  |  | Indicates whether the outlier for the discrete task assay is the difference from the mean outlier or SDI outlier. A value of 0 indicates the difference is from the SDI outlier. A value of 1 indicates the difference is from the mean. |
| 7 | `ROUND_ROBIN_REF_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the round robin template associated with the discrete task assay. Creates a relationship to the round robin reference table. |
| 8 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific service resource (i.e. instrument, bench, etc.) that is associated with the round robin template. |
| 9 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific discrete task assay associated with the round robin template. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ROUND_ROBIN_REF_ID` | [ROUND_ROBIN_REF](ROUND_ROBIN_REF.md) | `ROUND_ROBIN_REF_ID` |

