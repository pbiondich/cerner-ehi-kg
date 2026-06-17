# RX_COA_TRANS_AUDIT

> Audits the COA transactions without logging the servers for improved troubleshooting.

**Description:** Pharmacy Charge on Administration Transaction Audit  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_TXT` | LONGTEXT |  |  | Stores audit text information captured by charge/credit workflows; |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | Contains the date and time this record was created. |
| 3 | `EVENT_ID` | DOUBLE |  |  | Identifies the Clinical Event related to COA transactions audited. |
| 4 | `ORDER_ID` | DOUBLE |  | FK→ | Identifies Orders related to COA transactions audited. |
| 5 | `RX_COA_TRANS_AUDIT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RX_COA_TRANS_AUDIT table. |
| 6 | `SCRIPT_NAME` | VARCHAR(32) |  |  | Stores the script name through which transaction occurs; |
| 7 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

