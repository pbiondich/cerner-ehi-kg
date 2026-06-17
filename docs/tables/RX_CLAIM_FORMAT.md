# RX_CLAIM_FORMAT

> Details Prescription claim formats

**Description:** RX CLAIM FORMAT  
**Table type:** REFERENCE  
**Primary key:** `FORMAT_ID`  
**Columns:** 23  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLAIM_SEGMENT_CD` | DOUBLE | NOT NULL |  | The code value of the claim segment that contains the claim field. |
| 2 | `FIELD_BEG_POS` | DOUBLE |  |  | CLAIM FIELD BEGINNING POSITION |
| 3 | `FIELD_CD` | DOUBLE | NOT NULL |  | CODE VALUE FROM CODE SET 4517 |
| 4 | `FIELD_DECIMAL_CNT` | DOUBLE |  |  | NUMBER OF DIGITS AFTER DECIMAL TO BE USED |
| 5 | `FIELD_END_POS` | DOUBLE |  |  | CLAIM FIELD ENDING POSITION |
| 6 | `FIELD_LENGTH` | DOUBLE |  |  | LENGTH OF CLAIM FIELD |
| 7 | `FIELD_TYPE_FLAG` | DOUBLE |  |  | Field_Type Flag (1-Alpha,2-Alpha/Numeric,3-Numeric,4-Decimal) |
| 8 | `FORMAT_CD` | DOUBLE | NOT NULL |  | CODE VALUE FROM CODE SET 4515 |
| 9 | `FORMAT_ID` | DOUBLE | NOT NULL | PK | UNIQUE ID FOR EACH FIELD IN THE FORMAT |
| 10 | `FORMAT_SEQ` | DOUBLE |  |  | SEQUENCE OF THE FIELDS IN THE FORMAT |
| 11 | `FORMAT_TYPE_CD` | DOUBLE | NOT NULL |  | CODE VALUE FROM CODE SET 4516 |
| 12 | `REQUIRED_IND` | DOUBLE |  |  | INDICATOR (0 OR 1). indicates whether or not a the field is required for the format. (1=Required) |
| 13 | `REVERSAL_REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates whether the field is required during claim reversal transaction. (1 = required, 0 = not required.) |
| 14 | `SOURCE_BEG_POS` | DOUBLE |  |  | The position of the character, in the Source value, that is used as the starting point. |
| 15 | `SOURCE_END_POS` | DOUBLE |  |  | CLAIM SOURCE ENDING POSITION |
| 16 | `SOURCE_FIELD_CD` | DOUBLE | NOT NULL |  | CODE VALUE FROM CODE SET 4518 |
| 17 | `SOURCE_STRING` | VARCHAR(255) |  |  | Value of the Source, if Source is a literal value. |
| 18 | `STANDARD_IND` | DOUBLE |  |  | INDICATOR (0 OR 1). indicates whether or not the format is modifiable. (1 = Not Modifiable) |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RX_HEALTH_PLAN_CLAIM](RX_HEALTH_PLAN_CLAIM.md) | `CLAIM_FORMAT_ID` |

