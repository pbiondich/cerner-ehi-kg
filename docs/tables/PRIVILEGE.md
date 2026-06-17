# PRIVILEGE

> This table contains a privilege that is being tied to a user, position or ppr.

**Description:** PRIVILEGE  
**Table type:** REFERENCE  
**Primary key:** `PRIVILEGE_ID`  
**Columns:** 15  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `LOG_GROUPING_CD` | DOUBLE | NOT NULL | FK→ | The privileges tool needs a way to associate exception groups to a privilege. Exception groups are currently stored on the logical_grouping and log_group_entry table. In order to keep track of this 1 to 1 relationship, we need to add the primary key of the logical_grouping table as a foreign key of the privilege table. |
| 6 | `PRIVILEGE_CD` | DOUBLE | NOT NULL |  | The code value representing the privilege. |
| 7 | `PRIVILEGE_ID` | DOUBLE | NOT NULL | PK | The unique identifier of a row on this table. |
| 8 | `PRIV_LOC_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The row on the privilege location relationship table that this privilege is tied to. |
| 9 | `PRIV_VALUE_CD` | DOUBLE | NOT NULL |  | The code value representing the granted access to this privilege, i.e. YES, NO, INCLUDE, EXCLUDE |
| 10 | `RESTR_METHOD_CD` | DOUBLE | NOT NULL |  | The code value representing the restriction method for this privilege, i.e. MASK or HIDE. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOG_GROUPING_CD` | [LOGICAL_GROUPING](LOGICAL_GROUPING.md) | `LOG_GROUPING_CD` |
| `PRIV_LOC_RELTN_ID` | [PRIV_LOC_RELTN](PRIV_LOC_RELTN.md) | `PRIV_LOC_RELTN_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [ACTIVITY_PRIVILEGE_RELTN](ACTIVITY_PRIVILEGE_RELTN.md) | `PRIVILEGE_ID` |
| [PRIVILEGE_DELETION](PRIVILEGE_DELETION.md) | `PRIVILEGE_ID` |
| [PRIVILEGE_EXCEPTION](PRIVILEGE_EXCEPTION.md) | `PRIVILEGE_ID` |
| [PRIV_GROUP_RELTN](PRIV_GROUP_RELTN.md) | `PRIVILEGE_ID` |

