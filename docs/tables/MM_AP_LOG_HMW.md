# MM_AP_LOG_HMW

> AP Log table for HLTH_MO only.

**Description:** MM AP LOG HMW  
**Table type:** ACTIVITY  
**Primary key:** `LOG_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_NBR` | DOUBLE |  |  | Batch Number |
| 2 | `BATCH_SELECTION` | VARCHAR(100) |  |  | Batch Selection |
| 3 | `COMMENTS` | VARCHAR(100) |  |  | Comments |
| 4 | `CREATE_APPLCTX` | DOUBLE |  |  | Application which created this row |
| 5 | `CREATE_DT_TM` | DATETIME |  |  | The date/time this entry was created. |
| 6 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 7 | `CREATE_TASK` | DOUBLE |  |  | Task which created this row |
| 8 | `FILENAME` | VARCHAR(100) |  |  | File Name |
| 9 | `LOG_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 10 | `OUTPUT_DIST` | VARCHAR(100) |  |  | Output Distribution (operations parameter) |
| 11 | `TOTAL_FREIGHT_AMT` | DOUBLE |  |  | Total Freight Amount |
| 12 | `TOTAL_GROSS_AMT` | DOUBLE |  |  | Total Gross Amount |
| 13 | `TOTAL_INVOICES` | DOUBLE |  |  | Total Invoices |
| 14 | `TOTAL_LINES` | DOUBLE |  |  | Total Invoice Lines |
| 15 | `TOTAL_LINE_AMT` | DOUBLE |  |  | Total line amount |
| 16 | `TOTAL_SALES_TAX_AMT` | DOUBLE |  |  | Total Sales Tax Amount |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MM_AP_LOG_HEADER_HMW](MM_AP_LOG_HEADER_HMW.md) | `LOG_ID` |

