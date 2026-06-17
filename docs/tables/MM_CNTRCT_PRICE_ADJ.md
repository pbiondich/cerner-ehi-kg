# MM_CNTRCT_PRICE_ADJ

> Contract Price Adjustment

**Description:** Contract Price Adjustment  
**Table type:** REFERENCE  
**Primary key:** `PRICE_ADJ_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADJUSTMENT` | DOUBLE |  |  | adjustment |
| 2 | `ADJ_METRIC_CD` | DOUBLE | NOT NULL |  | Adjustment metric code |
| 3 | `ADJ_TYPE_CD` | DOUBLE | NOT NULL |  | Adjustment type code value |
| 4 | `CLASS_NODE_ID` | DOUBLE | NOT NULL |  | Class Node ID value. |
| 5 | `CNTRCT_ID` | DOUBLE | NOT NULL | FK→ | Contract number key |
| 6 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 7 | `CREATE_DT_TM` | DATETIME |  |  | The date and time when the row was inserted |
| 8 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) who inserted the row in to the table. |
| 9 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 10 | `PRICE_ADJ_ID` | DOUBLE | NOT NULL | PK | price adjustment identifier |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNTRCT_ID` | [MM_CNTRCT_HDR](MM_CNTRCT_HDR.md) | `CNTRCT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MM_XFI_CNTRCT_PRICE_ADJ](MM_XFI_CNTRCT_PRICE_ADJ.md) | `PRICE_ADJ_ID` |

