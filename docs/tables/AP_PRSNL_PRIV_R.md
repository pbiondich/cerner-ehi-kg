# AP_PRSNL_PRIV_R

> This table holds the individuals and/or user groups that an AP user has granted a specific privilege.

**Description:** AP Personnel Privileges Resolution  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the 'ap_prsnl_priv' row is related (PRSNL_GROUP_ID from the PRSNL_GROUP table, PERSON_ID from the PRSNL table). |
| 2 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The upper case name of the table to which this 'ap_prsnl_priv' row is related. Valid values for this column are PRSNL_GROUP and PRSNL. |
| 3 | `PRIVILEGE_ID` | DOUBLE | NOT NULL |  | This field contains the foreign key value used to join to AP_PRSNL_PRIV table. |
| 4 | `PROXY_BEG_DT_TM` | DATETIME |  |  | Displays the date when the assigned proxy begins. |
| 5 | `PROXY_END_DT_TM` | DATETIME |  |  | Displays the date when the assigned proxy ends. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

