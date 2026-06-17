# ORG_ORG_RELTN

> The organization-organization relationship table contains the relationships of independent organizations to each other. For example, XYZ Physician Office is a client of ABC Reference Lab.

**Description:** Organization Organization Relationship  
**Table type:** REFERENCE  
**Primary key:** `ORG_ORG_RELTN_ID`  
**Columns:** 20  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COMMENT_TEXT` | LONGTEXT |  |  | Future Use |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 9 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 10 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 13 | `ORG_ORG_RELTN_CD` | DOUBLE | NOT NULL |  | Identifies the specific type of relationship between two independent organizations. This field is user defined (I.e., client, contractor, etc.). |
| 14 | `ORG_ORG_RELTN_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the organization organization relationship table. It is an internal system assigned number. |
| 15 | `RELATED_ORG_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. This is a 'role' name for the reference to organization_id in the organization table and used to differentiate between other references to organization_id in this table. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `RELATED_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ORG_ORG_RELTN_INFO](ORG_ORG_RELTN_INFO.md) | `ORG_ORG_RELTN_ID` |

