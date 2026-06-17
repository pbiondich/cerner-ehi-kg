# PERSON_PRSNL_ORG_OVERRIDE

> The person personnel organization override table contains information regarding a personnel's permission to access a patient's data at a particular organization which overrides organization security.

**Description:** Person Personnel Organization Override  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHART_ACCESS_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the chart access organization which contains the data of the patient that the personnel is requesting persmission to access. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person identifier of the patient to which the personnel requests permission to access data. |
| 9 | `PERSON_PRSNL_ORG_OVERRIDE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the PERSON_PRSNL_ORG_OVERRIDE table. |
| 10 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel identifier of the user requesting access to patient data associated with the organization. |
| 11 | `SOURCE_CHILD_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the source child organization from where the personnel requests permission to access data. This is also used to limit the scope of the access being granted. This would be optional and not be needed in most workflows. For Sweden workflows, this would be the care unit. |
| 12 | `SOURCE_PARENT_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the source parent organization from where the personnel requests permission to access data. This is also used to limit the scope of the access being granted. This would be optional and not be needed in most workflows. For Sweden workflows, this would be the care giver. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_ACCESS_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SOURCE_CHILD_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `SOURCE_PARENT_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

