# RAD_FOREIGN_REQ_ITEMS

> The Rad_Foreign_Req_Items table contains information about specific items that have been requested from an outside source.

**Description:** Rad Foreign Request Items  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RAD_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | The Rad_Request_Id is a foreign key to the Rad_Request table. It identifies the Request that the foreign request item is a part of. |
| 2 | `REQUEST_ITEM` | VARCHAR(255) |  |  | The Request_Item is a textual description of the item that is being requested. |
| 3 | `SEQUENCE` | DOUBLE | NOT NULL |  | The Sequence combined with the Rad_Request_Id uniquely identifies a row in the Rad_Foreign_Req_Items table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RAD_REQUEST_ID` | [RAD_REQUEST](RAD_REQUEST.md) | `RAD_REQUEST_ID` |

