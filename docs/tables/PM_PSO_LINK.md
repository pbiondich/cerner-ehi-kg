# PM_PSO_LINK

> A temporary staging table to hold orders transaction data to work around limitations within Orders physician selection UI and EKM/Discern's ability to modify order details during the sign order event.

**Description:** Patient Management Patient Status Orders Link  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CREATE_DT_TM` | DATETIME |  |  | This is the date and time that the row was created. |
| 6 | `LINK_STATUS_CD` | DOUBLE | NOT NULL |  | Contains the value of the status of the link. |
| 7 | `OE_FIELD_DISPLAY_VALUE` | VARCHAR(255) |  |  | The display value of the order detail. |
| 8 | `OE_FIELD_DT_TM_VALUE` | DATETIME |  |  | The date and time value of the field if of type date/time. |
| 9 | `OE_FIELD_ID` | DOUBLE | NOT NULL |  | The id of the field. |
| 10 | `OE_FIELD_MEANING` | VARCHAR(25) |  |  | The meaning of the field. |
| 11 | `OE_FIELD_MEANING_ID` | DOUBLE | NOT NULL | FK→ | The Cerner controlled value that id's the meaning of the field. |
| 12 | `OE_FIELD_VALUE` | DOUBLE |  |  | The value of the field if a numeric or coded value. |
| 13 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The id of the order. |
| 14 | `PM_PSO_LINK_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the PM_PSO_LINK table. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OE_FIELD_MEANING_ID` | [OE_FIELD_MEANING](OE_FIELD_MEANING.md) | `OE_FIELD_MEANING_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

