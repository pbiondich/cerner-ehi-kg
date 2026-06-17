# BR_DATAM_VAL_SET_ITEM

> Links a value set with the vocabulary coding system items.

**Description:** Bedrock Datamart Value Set Item  
**Table type:** REFERENCE  
**Primary key:** `BR_DATAM_VAL_SET_ITEM_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `BR_DATAM_VAL_SET_ID` | DOUBLE | NOT NULL | FK→ | The value set that is linked to this coding system item. |
| 3 | `BR_DATAM_VAL_SET_ITEM_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that uniquely identifies a single row on the BR_DATAM_VAL_SET_ITEM table. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `SOURCE_VOCAB_ITEM_IDENT` | VARCHAR(50) | NOT NULL |  | The code for the EHR Measure. This corresponds to a source_identifier on the Nomenclature table. |
| 6 | `SOURCE_VOCAB_MEAN` | VARCHAR(12) | NOT NULL |  | The coding system used for the EHR Measure code. This corresponds to a source vocabulary code on the nomenclature table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_DATAM_VAL_SET_ID` | [BR_DATAM_VAL_SET](BR_DATAM_VAL_SET.md) | `BR_DATAM_VAL_SET_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_DATAM_VAL_SET_ITEM_MEAS](BR_DATAM_VAL_SET_ITEM_MEAS.md) | `BR_DATAM_VAL_SET_ITEM_ID` |

