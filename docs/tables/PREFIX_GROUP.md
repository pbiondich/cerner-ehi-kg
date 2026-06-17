# PREFIX_GROUP

> This reference table contains parameters specific to pathology prefix groups. A group represents a set of sequential numbers, and includes parameters such as the option to reset the numbers yearly. One or more prefixes can be included a single group.

**Description:** Prefix Group  
**Table type:** REFERENCE  
**Primary key:** `GROUP_ID`  
**Columns:** 12  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `GROUP_DESC` | VARCHAR(40) |  |  | This field contains the description of the accession group. |
| 3 | `GROUP_ID` | DOUBLE | NOT NULL | PK FK→ | This field contains the foreign key value used to represent the accession group. |
| 4 | `GROUP_NAME` | CHAR(2) |  |  | This field contains the short name (mnemonic) representing the prefix group value. |
| 5 | `MANUAL_ASSIGN_IND` | DOUBLE |  |  | This field contains a flag value documenting whether or not case numbers assigned from this accession group can be manually assigned (manually entered) by the user. |
| 6 | `RESET_YEARLY_IND` | DOUBLE |  |  | This field contains a flag value documenting whether or not case numbers assigned from this accession group should automatically be reset to 1 for the first case of a new year. |
| 7 | `SITE_CD` | DOUBLE | NOT NULL |  | This field contains a reference to the accession site code associated with the accession group. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GROUP_ID` | [ACCESSION_ASSIGN_POOL](ACCESSION_ASSIGN_POOL.md) | `ACCESSION_ASSIGNMENT_POOL_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [AP_PREFIX](AP_PREFIX.md) | `GROUP_ID` |
| [PATHOLOGY_CASE](PATHOLOGY_CASE.md) | `GROUP_ID` |

