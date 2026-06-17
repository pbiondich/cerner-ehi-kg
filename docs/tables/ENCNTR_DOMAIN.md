# ENCNTR_DOMAIN

> The encounter domain table contains key information used to provide a specific domain view of a setof encounters (i.e., hospital census). A row in the encounter domain table will generally get created or deleted as the result of an ADT related event.

**Description:** Encounter Domain  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `ENCNTR_DOMAIN_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the encounter domain table. It is an internal system assigned number. |
| 7 | `ENCNTR_DOMAIN_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the access path or index (I.e., nurse unit/room/bed) for a set or list of encounters in the encounter table. The set of encounters is determined by adding or deleting rows in this table when events (I.e., ATDs, etc.) occur in the system. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `LOC_BED_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of bed. |
| 11 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of building. |
| 12 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of facility. |
| 13 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of nurse unit. |
| 14 | `LOC_ROOM_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of room. |
| 15 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | The category of treatment, surgery, or general resources. |
| 16 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LOC_BED_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_BUILDING_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_ROOM_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

