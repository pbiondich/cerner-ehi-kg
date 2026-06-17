# COMMITTEE

> This table contains the information about the committees

**Description:** This table contains information about committees.  
**Table type:** REFERENCE  
**Primary key:** `COMMITTEE_ID`  
**Columns:** 12  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `COMMITTEE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the committee table. It is an internal system assigned number. |
| 3 | `COMMITTEE_NAME` | VARCHAR(255) | NOT NULL |  | Name of the committee |
| 4 | `COMMITTEE_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of committee. Valid values are IRB, CPSRMC and OTHER. |
| 5 | `EMAIL_ADDRESS` | VARCHAR(255) |  |  | E-mail address of the committee |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `SPONSORING_ORG_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SPONSORING_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [COMMITTEE_MEMBER](COMMITTEE_MEMBER.md) | `COMMITTEE_ID` |
| [CT_DEFAULT_MILESTONES](CT_DEFAULT_MILESTONES.md) | `COMMITTEE_ID` |
| [CT_MILESTONES](CT_MILESTONES.md) | `COMMITTEE_ID` |
| [CT_PROT_MILESTONES](CT_PROT_MILESTONES.md) | `COMMITTEE_ID` |
| [CT_TYPE_COMMITTEE_RELTN](CT_TYPE_COMMITTEE_RELTN.md) | `COMMITTEE_ID` |
| [PROT_AMD_COMMITTEE_RELTN](PROT_AMD_COMMITTEE_RELTN.md) | `COMMITTEE_ID` |

