# MIC_STAT_DUPLICATE

> This table contains Microbiology orders, previously written to the Microbiology statistical data model, that require the report and susceptibility duplicate checking to be re-evaluated.

**Description:** Microbiololgy Statistical Duplicate  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLLECT_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time at which the orderable procedure was collected. |
| 2 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique value assigned to each orderable procedure associated with an order. For example: if there are two procedures on the same accession number, then each procedure will have a unique order id. |
| 3 | `PROCESS_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the process, which triggered the archiving of the order. This field contains a non-zero value only when archiving is triggered from the Statistical Preference tool. This could be used to join to the MIC_STAT_PROCESS table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PROCESS_ID` | [MIC_STAT_PROCESS](MIC_STAT_PROCESS.md) | `PROCESS_ID` |

