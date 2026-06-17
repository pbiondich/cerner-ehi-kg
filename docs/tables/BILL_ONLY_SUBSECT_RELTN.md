# BILL_ONLY_SUBSECT_RELTN

> The Bill_Only_Subsect_Reltn table contains the relationship between a sub section and a bill only or bill only category.

**Description:** Bill Only Sub Section Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENTITY_ID` | DOUBLE | NOT NULL |  | The Entity_Id contains a primary key from one of a couple of tables. It along with the Entity_Name identifies the bill only or bill only category that is associated with this procedure. |
| 2 | `ENTITY_NAME` | VARCHAR(40) | NOT NULL |  | The Entity_Name contains the table name that corresponds with the Entity_Id. It along with the Entity_Id identifies the bill only or bill only category that is associated with this procedure. |
| 3 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The Service_Resource_Cd is a foreign key to the Sub_Section table. It identifies the sub section that has the bill only or bill only category associated with it. |
| 4 | `STANDARD_QTY` | DOUBLE |  |  | The Standard_Qty contains the standard number, of this specific bill only, that is used. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

