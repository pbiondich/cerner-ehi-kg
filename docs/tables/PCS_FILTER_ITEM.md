# PCS_FILTER_ITEM

> This table stores the specific filter items for a given personal filter.

**Description:** Selected filter items.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `FILTER_DT_TM` | DATETIME |  |  | Holds the date and time that is associated with a given filter. |
| 8 | `FILTER_ID` | DOUBLE | NOT NULL | FK→ | Contains the internal identification code that uniquely identifies the personal filter. This field is used to join to other tables such as PCS_PRSNL_FILTER table. |
| 9 | `FILTER_TYPE_CD` | DOUBLE | NOT NULL |  | Defines the type of filter select (i.e. order catalog code, queue review status, etc.) Filter types are defined in code set 29244 |
| 10 | `FILTER_VALUE` | DOUBLE | NOT NULL |  | Holds a double that is associated with the given filter. |
| 11 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | id number of the selected criteria located on table . |
| 12 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Table name where selected criteria is stored. Valid names include:CODE_VALUE, ORDER_CATALOG |
| 13 | `SELECTED_ITEM_ID` | DOUBLE | NOT NULL |  | Contains the internal identification code that uniquely identifies a selected filter item. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FILTER_ID` | [PCS_PRSNL_FILTER](PCS_PRSNL_FILTER.md) | `FILTER_ID` |

