# ORDER_ENTRY_FORMAT_PARENT

> Stores the format that will be associated to an orderable to identify the information to be captured at order time.

**Description:** Order entry format parent.  
**Table type:** REFERENCE  
**Primary key:** `OE_FORMAT_ID`  
**Columns:** 8  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | Codified value for order catalog type. |
| 2 | `OE_FORMAT_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the order entry format. |
| 3 | `OE_FORMAT_NAME` | VARCHAR(200) | NOT NULL |  | The name of the order entry format. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (6)

| From table | Column |
|------------|--------|
| [ORDERS](ORDERS.md) | `OE_FORMAT_ID` |
| [ORDER_CATALOG](ORDER_CATALOG.md) | `OE_FORMAT_ID` |
| [ORDER_PROPOSAL](ORDER_PROPOSAL.md) | `OE_FORMAT_ID` |
| [ORDER_SENTENCE](ORDER_SENTENCE.md) | `OE_FORMAT_ID` |
| [SCH_APPT_TYPE](SCH_APPT_TYPE.md) | `OE_FORMAT_ID` |
| [SCH_REPORT](SCH_REPORT.md) | `OE_FORMAT_ID` |

