# ORG_CONTRIBUTOR_SYS_RELTN

> The organization-contributor system relationship table contains the relationships between organizations from the organization table and contributor systems from the contributor system table. The kind of relationships defines how the organization and contributor system are related.

**Description:** Organization Contributor System Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AUTHORIZATION_TYPE_CD` | DOUBLE | NOT NULL |  | The standard used to determine if the organization is authorized to access the contributing system |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CONSENT_POLICY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the ppr_consent_policy table to identify the policy associated with the contributor system and organization |
| 5 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL | FK→ | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 6 | `DOMAIN_ADDR` | VARCHAR(255) | NOT NULL |  | A URL associated with the contributing system |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `INFO_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | This column stores what type of information is written to the row. |
| 9 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 10 | `ORG_CONTRIBUTOR_SYS_RELTN_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the organization-contributor system relationship table. It is an internally assigned number and generally not revealed to the user. |
| 11 | `RELTN_TYPE_CD` | DOUBLE | NOT NULL |  | Code value indicating the type of relationship (I.e., PHR) |
| 12 | `UDF_CONSENT_CD` | DOUBLE | NOT NULL |  | Contains the user defined, granted consent code value. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONSENT_POLICY_ID` | [PPR_CONSENT_POLICY](PPR_CONSENT_POLICY.md) | `CONSENT_POLICY_ID` |
| `CONTRIBUTOR_SYSTEM_CD` | [CONTRIBUTOR_SYSTEM](CONTRIBUTOR_SYSTEM.md) | `CONTRIBUTOR_SYSTEM_CD` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

