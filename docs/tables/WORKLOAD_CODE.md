# WORKLOAD_CODE

> workload code

**Description:** Stores workload codes  
**Table type:** REFERENCE  
**Primary key:** `WORKLOAD_CODE_ID`  
**Columns:** 23  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CODE` | VARCHAR(50) |  |  | The workload code, eventually this will be tied back to nomenclature. |
| 7 | `DESCRIPTION` | VARCHAR(200) |  |  | The description of the workload code. This would usually come directly from the standard. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `EVENT_CD` | DOUBLE | NOT NULL |  | Value from 13029 that represents the event that will trigger this workload code. |
| 10 | `INTERVAL_TEMPLATE_CD` | DOUBLE | NOT NULL |  | Value from 14274 that represents the intervals to be used in calculating the workload units to accrue for a particular workload code for this unit_type. |
| 11 | `ITEM_FOR_COUNT_CD` | DOUBLE | NOT NULL |  | The code value from codeset 15229 that shows the recommended method for counting workload for this code. Examples include plate/bottle/tube, test, analyte, specimen, person, etc. |
| 12 | `LABOR_TYPE` | DOUBLE |  |  | not used |
| 13 | `MULTIPLIER` | DOUBLE |  |  | Number by which to multiply the number of units. |
| 14 | `NOMEN_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the nomenclature table. It is an internal system assigned number. |
| 15 | `NOTE` | VARCHAR(200) |  |  | Free text area for the user to enter extra notes that are either specific to the organization's use of this workload code, or could be extra notes that are defined in the standard. |
| 16 | `UNITS` | DOUBLE |  |  | Number of units. This is usually the value recommended by the standard. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `WORKLOAD_CODE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the workload_code table. It is an internal system assigned number. |
| 23 | `WORKLOAD_STANDARD_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the workload_standard table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WORKLOAD_STANDARD_ID` | [WORKLOAD_STANDARD](WORKLOAD_STANDARD.md) | `WORKLOAD_STANDARD_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [WORKLOAD_GROUP](WORKLOAD_GROUP.md) | `WORKLOAD_CODE_ID` |

