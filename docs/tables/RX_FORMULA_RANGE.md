# RX_FORMULA_RANGE

> Stores criteria information used for selecting formulas

**Description:** PharmNet Formula Range  
**Table type:** REFERENCE  
**Primary key:** `RX_FORMULA_RANGE_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DEMOG_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag for determining what type of demographic is stored on this row (age, weight, height, serum creatinine, result ) |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `ETHNICITY_CD` | DOUBLE | NOT NULL |  | The ethnicity that this formula pertains to. |
| 6 | `GENDER_CD` | DOUBLE | NOT NULL |  | The gender that this formula pertains to. |
| 7 | `MAX_VALUE` | DOUBLE |  |  | The maximum value for the formula. |
| 8 | `MIN_VALUE` | DOUBLE |  |  | The minimum value for the formula. |
| 9 | `OPERATOR_FLAG` | DOUBLE | NOT NULL |  | Indicates which mathematical operator is stored on this row. (<. between, >) |
| 10 | `RACE_CD` | DOUBLE | NOT NULL |  | The race that this formula pertains to. |
| 11 | `RX_FORMULA_ID` | DOUBLE | NOT NULL | FK→ | The formula this range is related to. |
| 12 | `RX_FORMULA_RANGE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RX_FORMULA_RANGE table. |
| 13 | `RX_FORMULA_RANGE_P_ID` | DOUBLE | NOT NULL | FK→ | Used for groupings versions of a Formula Range. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `VALUE_UOM_CD` | DOUBLE | NOT NULL |  | The unit code for the given values. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RX_FORMULA_ID` | [RX_FORMULA](RX_FORMULA.md) | `RX_FORMULA_ID` |
| `RX_FORMULA_RANGE_P_ID` | [RX_FORMULA_RANGE](RX_FORMULA_RANGE.md) | `RX_FORMULA_RANGE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RX_FORMULA_RANGE](RX_FORMULA_RANGE.md) | `RX_FORMULA_RANGE_P_ID` |

