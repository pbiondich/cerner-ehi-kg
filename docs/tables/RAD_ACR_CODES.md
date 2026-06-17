# RAD_ACR_CODES

> The Rad_ACR_Codes table contains the ACR codes that have been associated with an order.

**Description:** Rad ACR Codes  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACR_STRING` | VARCHAR(15) |  |  | This column is no longer used. |
| 2 | `ANATOMY_STR` | VARCHAR(15) |  |  | This column stores the anatomy piece of the ACR code. |
| 3 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The Order_Id field is a foreign key to the Order_Radiology table. It links the ACR code(s) to a specific order. |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The Parent_entity_id along with the parent_entity_name identifies the exam or order that the acr codes refer to |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The parent_entity_name along with the parent_entity_id identifies the exam or order that the acr codes refer to. |
| 6 | `PATHOLOGY_STR` | VARCHAR(15) |  |  | This column contains the Pathology piece of the ACR Code. |
| 7 | `PROC_CODE_STR` | VARCHAR(5) |  |  | This column contains the procedure code piece of the ACR string if one is specified. |
| 8 | `SEQUENCE` | DOUBLE | NOT NULL |  | The sequence column ensures that we have a unique primary key when partnered with the order_id. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `ORDER_ID` |

