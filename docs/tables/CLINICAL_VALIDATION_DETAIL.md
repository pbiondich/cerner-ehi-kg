# CLINICAL_VALIDATION_DETAIL

> This table stores the chronological ranges for which clinical data is valid for different age groups.

**Description:** Clinical Validation Detail  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AGE_MAX_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure associated with the maximum age value. |
| 3 | `AGE_MAX_VALUE` | DOUBLE | NOT NULL |  | The maximum age contained within this range. |
| 4 | `AGE_MIN_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure associated with the minimum age value. |
| 5 | `AGE_MIN_VALUE` | DOUBLE | NOT NULL |  | The minimum age contained within this range. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CLINICAL_VALIDATION_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the Validation_Detail table. |
| 8 | `CLINICAL_VALIDATION_ID` | DOUBLE | NOT NULL | FK→ | The primary key on the Clinical_Validation table |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `RANGE_UNIT_CD` | DOUBLE | NOT NULL |  | The duration code value associated with the range. |
| 11 | `RANGE_VALUE` | DOUBLE | NOT NULL |  | The amount of time to subtract from now to determine if a clinical event is valid. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLINICAL_VALIDATION_ID` | [CLINICAL_VALIDATION](CLINICAL_VALIDATION.md) | `CLINICAL_VALIDATION_ID` |

