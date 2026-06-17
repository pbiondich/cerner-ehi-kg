# CT_DEFAULT_MILESTONES

> This table contains default milestones for protocol, amendment, concept etc..

**Description:** CT DEFAULT MILESTONES  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_CD` | DOUBLE | NOT NULL |  | The activity related to the milestone. Example: Activated By, Approved By etc. |
| 2 | `COMMITTEE_ID` | DOUBLE | NOT NULL | FK→ | The committee performing the milestone activity |
| 3 | `CT_DEFAULT_MILESTONES_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ct_default_milestones table. It is an internal system assigned number. |
| 4 | `DEFAULT_LIST_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates that type of milestone. Whether it is a milestone for a protocol, or amendment or concept and so on. |
| 5 | `ENTITY_TYPE_FLAG` | DOUBLE | NOT NULL |  | Used to identify whether an Organization or Committee or role performed the activity. |
| 6 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 7 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The Organization that performed the activity. This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 8 | `PROT_ROLE_CD` | DOUBLE | NOT NULL |  | Identifies the role performing the activity |
| 9 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | The number of the milestone |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMITTEE_ID` | [COMMITTEE](COMMITTEE.md) | `COMMITTEE_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

