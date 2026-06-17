# FORM_ASSOCIATION

> Contains the association between a input form and an order catalog item or an order task

**Description:** Form Association  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSOCIATION_TYPE_FLAG` | DOUBLE |  |  | An indicator of the type of association, i.e. Order Catalog, Order Task |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The order catalog entry associated with this input form (when the association_type_flag = 1) |
| 3 | `FORM_ASSOCIATION_ID` | DOUBLE | NOT NULL |  | The primary key, uniquely identifying a row on this table |
| 4 | `INPUT_FORM_CD` | DOUBLE | NOT NULL |  | The input form code referred to in this form association |
| 5 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The location associated with this form association |
| 6 | `ORDER_TYPE_FLAG` | DOUBLE |  |  | NOT CURRENTLY BEING USED |
| 7 | `REFERENCE_TASK_ID` | DOUBLE | NOT NULL |  | A reference (foreign key) to the order_task table indicating the order task associated with this form (when association_type_flag=2) |
| 8 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | NOT BEING USED |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |

