# RX_METHOD_RANGE

> Contains ranges of values that the Method is valid for. For example, a method might only be valid for use with persons 18 years or older.

**Description:** PharmNet Method Range  
**Table type:** REFERENCE  
**Primary key:** `RX_METHOD_RANGE_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DEMOG_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag for determining what type of demographic is stored on this row (age, weight, height, serum creatinine, result ) |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `MAX_VALUE` | DOUBLE |  |  | The maximum value for the range. |
| 6 | `MIN_VALUE` | DOUBLE |  |  | The minimum value for the range. |
| 7 | `RX_METHOD_ID` | DOUBLE | NOT NULL | FK→ | The method this range is related to. |
| 8 | `RX_METHOD_RANGE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RX_METHOD_RANGE table. |
| 9 | `RX_METHOD_RANGE_P_ID` | DOUBLE | NOT NULL | FK→ | Used to group versions of Method Ranges. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VALUE_UOM_CD` | DOUBLE | NOT NULL |  | The unit code for the given values. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RX_METHOD_ID` | [RX_METHOD](RX_METHOD.md) | `RX_METHOD_ID` |
| `RX_METHOD_RANGE_P_ID` | [RX_METHOD_RANGE](RX_METHOD_RANGE.md) | `RX_METHOD_RANGE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RX_METHOD_RANGE](RX_METHOD_RANGE.md) | `RX_METHOD_RANGE_P_ID` |

