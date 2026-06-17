# PRSNL_ORG_RELTN_TYPE

> This table will store a PRSNL's link to ORGANIZATIONs and it will give the ability to specify a type on the relationship. This table is not used for Org security. The PRSNL_ORG_RELTN table is used for that.

**Description:** Personnel/Organization relationship type  
**Table type:** REFERENCE  
**Primary key:** `PRSNL_ORG_RELTN_TYPE_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESS_POSITION_CD` | DOUBLE | NOT NULL |  | access position code value |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `JOB_ROLE_CD` | DOUBLE | NOT NULL |  | Descibes the personnel's job as related to this organization; e.g., Cardiac Surgeon or Physical Therapist. |
| 10 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization that has a relationship with the personnel. |
| 11 | `ORG_TYPE_CD` | DOUBLE | NOT NULL |  | The type of organization that the organization is playing when the personnel to organization relationship type (prsnl_org_reltn_type_cd) is valid. |
| 12 | `POSITION_CD` | DOUBLE | NOT NULL |  | The position the personnel is playing when the personnel to organization relationship type (prsnl_org_reltn_type_cd) is valid. |
| 13 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that has a relationship with the organization. |
| 14 | `PRSNL_ORG_RELTN_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the specific type of relationship of the personnel to the organization. |
| 15 | `PRSNL_ORG_RELTN_TYPE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the prsnl_org_reltn_type table. It is an internal system assigned number. |
| 16 | `ROLE_PROFILE` | VARCHAR(255) |  |  | Identifies the role profile that contains this organization and position. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PRSNL_ROLE_PROFILE_ADDN](PRSNL_ROLE_PROFILE_ADDN.md) | `PRSNL_ORG_RELTN_TYPE_ID` |

