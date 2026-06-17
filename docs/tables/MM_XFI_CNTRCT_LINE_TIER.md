# MM_XFI_CNTRCT_LINE_TIER

> Table used to store relationships between contracts and line price tiers. Data is moved from this table to MM_CNTRCT_LINE_TIER.

**Description:** MM XFI CNTRCT LINE TIER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE |  |  | Flag used to determine how the tier will be processed |
| 2 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the record was created |
| 4 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 5 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 6 | `DISCOUNT` | DOUBLE |  |  | discount |
| 7 | `HDR_PRICE_TIER_ID` | DOUBLE | NOT NULL |  | header price tier identifier |
| 8 | `PRICE_TIER_ID` | DOUBLE | NOT NULL | FK→ | price tier identifier value |
| 9 | `PROCESS_FLAG` | DOUBLE |  |  | process flag |
| 10 | `TRANSACTION_ID` | DOUBLE | NOT NULL |  | Primary key |
| 11 | `TRANS_PARENT_ID` | DOUBLE | NOT NULL | FK→ | transaction parent identifier |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRICE_TIER_ID` | [MM_CNTRCT_LINE_TIER](MM_CNTRCT_LINE_TIER.md) | `PRICE_TIER_ID` |
| `TRANS_PARENT_ID` | [MM_XFI_CNTRCT_LINE](MM_XFI_CNTRCT_LINE.md) | `TRANSACTION_ID` |

