# MM_CNTRCT_LINE_TIER

> Contract line tier

**Description:** Contract line tier  
**Table type:** REFERENCE  
**Primary key:** `PRICE_TIER_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CNTRCT_LINE_ID` | DOUBLE | NOT NULL | FK→ | contract line identifier |
| 2 | `CREATE_APPLCTX` | DOUBLE |  |  | Application which created this row |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | The date and time when the row was inserted |
| 4 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) who inserted the row in to the table. |
| 5 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 6 | `DISCOUNT` | DOUBLE |  |  | discount |
| 7 | `HDR_PRICE_TIER_ID` | DOUBLE | NOT NULL | FK→ | header price tier identifier |
| 8 | `PRICE_TIER_ID` | DOUBLE | NOT NULL | PK | price tier identifier value |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNTRCT_LINE_ID` | [MM_CNTRCT_LINE](MM_CNTRCT_LINE.md) | `CNTRCT_LINE_ID` |
| `HDR_PRICE_TIER_ID` | [MM_CNTRCT_HDR_TIER](MM_CNTRCT_HDR_TIER.md) | `PRICE_TIER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MM_XFI_CNTRCT_LINE_TIER](MM_XFI_CNTRCT_LINE_TIER.md) | `PRICE_TIER_ID` |

