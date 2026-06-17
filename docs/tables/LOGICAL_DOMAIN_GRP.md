# LOGICAL_DOMAIN_GRP

> This table is used to group various domains into logical groups. One use of this would be to assign authority by logical domain group which would allow a user to access the data for more than one domain

**Description:** Logical Domain Group  
**Table type:** REFERENCE  
**Primary key:** `LOGICAL_DOMAIN_GRP_ID`  
**Columns:** 13  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `DESCRIPTION` | VARCHAR(255) | NOT NULL |  | The description of the logical domain group. |
| 6 | `LOGICAL_DOMAIN_GRP_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. |
| 7 | `MNEMONIC` | VARCHAR(100) | NOT NULL |  | A character string used to identify the logical domain group. |
| 8 | `MNEMONIC_KEY` | VARCHAR(100) | NOT NULL |  | The mnemonic in upper case with the non-alphanumeric characters removed. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [LOGICAL_DOMAIN_GRP_RELTN](LOGICAL_DOMAIN_GRP_RELTN.md) | `LOGICAL_DOMAIN_GRP_ID` |
| [PRSNL](PRSNL.md) | `LOGICAL_DOMAIN_GRP_ID` |

