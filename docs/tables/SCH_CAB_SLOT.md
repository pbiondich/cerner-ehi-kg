# SCH_CAB_SLOT

> This table is used for defining slots for choose and book services

**Description:** Scheduling choose and book slots  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALLOCATED_IND` | DOUBLE | NOT NULL |  | Allocated Clinician Indicator |
| 2 | `CAB_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the scheduling Choose and Book Service. |
| 3 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 4 | `DEF_APPT_DUR` | DOUBLE | NOT NULL |  | The default duration (in minutes) for this CAB slot. |
| 5 | `DISPLAY_SEQ` | DOUBLE | NOT NULL |  | The sequence of the display. |
| 6 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location of the Slot within a Service. |
| 7 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | slot priority code |
| 8 | `RESOURCE_CD` | DOUBLE | NOT NULL |  | The identifier for the resource. A resource is an item of limited availability. |
| 9 | `SLOT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the slot type. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CAB_SERVICE_ID` | [SCH_CAB_SERVICE](SCH_CAB_SERVICE.md) | `CAB_SERVICE_ID` |
| `SLOT_TYPE_ID` | [SCH_SLOT_TYPE](SCH_SLOT_TYPE.md) | `SLOT_TYPE_ID` |

