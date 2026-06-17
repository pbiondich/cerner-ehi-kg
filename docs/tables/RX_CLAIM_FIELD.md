# RX_CLAIM_FIELD

> Rx_claim_field - Defines fields on a Prescription claim format.

**Description:** RX CLAIM FIELD  
**Table type:** REFERENCE  
**Primary key:** `CLAIM_FIELD_CD`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLAIM_FIELD_CD` | DOUBLE | NOT NULL | PK | Claim Field Code value |
| 2 | `FIELD_DECIMAL_CNT` | DOUBLE |  |  | Number of digits after decimal to be used. |
| 3 | `FIELD_LENGTH` | DOUBLE |  |  | Field Length |
| 4 | `FIELD_TYPE_FLAG` | DOUBLE |  |  | Field_Type Flag (1-Alpha,2-Alpha/Numeric,3-Numeric,4-Decimal) |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RX_HEALTH_PLAN_CLAIM](RX_HEALTH_PLAN_CLAIM.md) | `CLAIM_FIELD_CD` |

