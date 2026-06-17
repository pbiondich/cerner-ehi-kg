# MM_APPROVAL_LOG

> Approvals DB update logging table.

**Description:** MM APPROVAL LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPROVAL_STATUS` | DOUBLE |  |  | Set to Rejected or Approved depending on the action taken by the approver. |
| 2 | `ITEM_DESC` | VARCHAR(100) |  |  | Item description. |
| 3 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Item definition table. |
| 4 | `ITEM_NBR` | VARCHAR(40) |  |  | Item number. |
| 5 | `LINE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Line item table. |
| 6 | `MM_APPROVAL_LOG_ID` | DOUBLE | NOT NULL |  | Primary Key. |
| 7 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Package type table. |
| 8 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Foreign key, the prsnl_id of the person from the personnel table (prsnl) |
| 9 | `REQUISITION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Requisition table. |
| 10 | `REQ_LINE_COST` | DOUBLE |  |  | Cost of the requisition line. |
| 11 | `REQ_LINE_PKG` | VARCHAR(40) |  |  | Package of the Requisition line. |
| 12 | `REQ_LINE_QTY` | DOUBLE |  |  | Requisition line quantity. |
| 13 | `REQ_LOC_CD` | DOUBLE | NOT NULL |  | Requisition Location Code Value |
| 14 | `REQ_NBR` | VARCHAR(40) |  |  | Requisition number. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LINE_ITEM_ID` | [LINE_ITEM](LINE_ITEM.md) | `LINE_ITEM_ID` |
| `PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REQUISITION_ID` | [REQUISITION](REQUISITION.md) | `REQUISITION_ID` |

