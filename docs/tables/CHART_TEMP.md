# CHART_TEMP

> This table is used with charting distributions to hold encounters that qualify and meet the demographic criteria. It is a temporary table.

**Description:** This table is used with charting distributions to hold encounters that qualify.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_DT_TM` | DATETIME |  |  | The beginning date and time to post for the chart request. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | Encounter create_dt_tm |
| 3 | `DISTRIBUTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the distribution_id running. |
| 4 | `DONT_USE_IND` | DOUBLE |  |  | Indicator on whether this encounter should be used or not. Also used for cross-encounter logic for determining which items to use based on exclude law logic. |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 6 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | identifies the type of Encounter |
| 7 | `LOC_BED_CD` | DOUBLE | NOT NULL |  | Encounter loc_bed_cd |
| 8 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL |  | Encounter loc_building_cd |
| 9 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | Encounter loc_facility_cd |
| 10 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | Encounter loc_nurse_unit_cd |
| 11 | `LOC_ROOM_CD` | DOUBLE | NOT NULL |  | Encounter loc_room_cd |
| 12 | `LOOKBACK_DT_TM` | DATETIME |  |  | Represents the lookback date and time to use when qualifying the encounter against the clinical_event table. |
| 13 | `NON_CE_BEGIN_DT_TM` | DATETIME |  |  | This date/time is stored temporarily during distribution processing to indicate this encounter's begin_dt_tm for non-clinical_event results. |
| 14 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Encounter organization_id |
| 15 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 16 | `USE_IND` | DOUBLE |  |  | Used for cross-encounter logic for determining which items to use based on include law logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISTRIBUTION_ID` | [CHART_DISTRIBUTION](CHART_DISTRIBUTION.md) | `DISTRIBUTION_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

