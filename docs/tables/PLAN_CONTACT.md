# PLAN_CONTACT

> Stores contact information for health plans and carriers

**Description:** PLAN CONTACT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CARRIER_ID` | DOUBLE |  | FK→ | Identifier for an insurance carrier that owns this contact |
| 7 | `DISPLAY_ORDER` | DOUBLE |  |  | Defines the display sequence of the plan contacts |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `HEALTH_PLAN_ID` | DOUBLE |  | FK→ | Identifies the health plan that owns this contact information |
| 10 | `NAME_FIRST` | VARCHAR(100) |  |  | This is the person's given first name. |
| 11 | `NAME_LAST` | VARCHAR(100) |  |  | This is the person's family name. |
| 12 | `NAME_MIDDLE` | VARCHAR(100) |  |  | This is the given middle name for the person. |
| 13 | `PARENT_CONTACT_ID` | DOUBLE |  |  | If this contact belongs to another contact, the ID of the owner |
| 14 | `PERSON_ID` | DOUBLE |  | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 15 | `PERSON_IND` | DOUBLE | NOT NULL |  | Indicates whether the contact is a person or not |
| 16 | `PLAN_CONTACT_ID` | DOUBLE | NOT NULL |  | Unique identifier for this plan contact |
| 17 | `TIER` | DOUBLE |  |  | Define the nesting level of a contact |
| 18 | `TITLE` | VARCHAR(100) |  |  | Person's title |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CARRIER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

