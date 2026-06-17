# UCM_KARYOTYPE

> Contains karyotype activity data

**Description:** Unified Case Manager - Karyotype  
**Table type:** ACTIVITY  
**Primary key:** `UCM_KARYOTYPE_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `KARYOTYPE_STATUS_FLAG` | DOUBLE | NOT NULL |  | Represents the status of the Karyotype. Whether it was validated, not validated(validation is turned off), or validation was overridden. 0 - Not Validated; 1 - Validated; 2 - Overridden |
| 6 | `KARYOTYPE_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the text information related to this karyotype. |
| 7 | `PREV_UCM_KARYOTYPE_ID` | DOUBLE | NOT NULL |  | Used to track versions of the karyotype information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 8 | `UCM_KARYOTYPE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a karyotype. |
| 9 | `UCM_REPORT_FIELD_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the report field where the karyotype was captured. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `VALIDATION_VERSION_TXT` | VARCHAR(10) |  |  | Indicates the version of the validation logic used when validating and associating concepts to this karyotype. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `KARYOTYPE_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `UCM_REPORT_FIELD_ID` | [UCM_REPORT_FIELD](UCM_REPORT_FIELD.md) | `UCM_REPORT_FIELD_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [UCM_KARYOTYPE_CONCEPT](UCM_KARYOTYPE_CONCEPT.md) | `UCM_KARYOTYPE_ID` |

