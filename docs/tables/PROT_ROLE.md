# PROT_ROLE

> Table stores all the roles assignments for an amendment

**Description:** PROT ROLE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `CREATED_BY_CTMS_IND` | DOUBLE | NOT NULL |  | Indicates whether the role is created by CTMS. 0 indicates that the role is manually created and 1 indicates that the role is created by CTMS. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the organization playing a role on the amendment |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 6 | `POSITION_CD` | DOUBLE | NOT NULL |  | The position is used to determine the applications and tasks the personnel is authorized to use |
| 7 | `PRIMARY_CONTACT_IND` | DOUBLE | NOT NULL |  | Indicates whether a role is the primary contact for the amendment. |
| 8 | `PRIMARY_CONTACT_RANK_NBR` | DOUBLE | NOT NULL |  | Defines the rank/order of primary contacts. |
| 9 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the amendment |
| 10 | `PROT_ROLE_CD` | DOUBLE | NOT NULL |  | The role which is played by the person/entity on the amendmentz |
| 11 | `PROT_ROLE_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 12 | `PROT_ROLE_TYPE_CD` | DOUBLE | NOT NULL |  | The Type of role played. eg., personal/Institutional |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |

