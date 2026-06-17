# RESULT_HASH

> A reference table of any results of components of interpretations, and their corresponding hash mark to be used in creating the interpretation pattern.

**Description:** Result Hash  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BIOHAZARD_IND` | DOUBLE | NOT NULL |  | This column will indicate whether or not the interpretation hash will set a donor product to a biohazard. |
| 6 | `DAYS_INELIGIBLE` | DOUBLE | NOT NULL |  | This field will be used for donor interpretations only. It will be used to indicate on temporary deferrals how long the deferral period should be. |
| 7 | `DONOR_ELIGIBILITY_CD` | DOUBLE | NOT NULL |  | This field is used to identify the donor's eligibility based on interpretation of the hash results. It is only used for blood bank donor product interpretations. |
| 8 | `DONOR_REASON_CD` | DOUBLE | NOT NULL |  | This is the reason that will post to the donor's record for the specific result. It will be used to further explain the donor's eligibility status. This field is only utilized by blood bank donor product orders. |
| 9 | `FROM_RESULT_RANGE` | DOUBLE |  |  | The lowest number in the range of numeric results for which this hash mark applies. This column only applies to numeric results. |
| 10 | `INCLUDED_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | The discrete task assay for which this hash mark applies. |
| 11 | `INTERP_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the INTERP_DETAIL table. An internal system-assigned number. On this table, it provides a link from the interpretation detail procedure to the hash marks for the results. |
| 12 | `INTERP_ID` | DOUBLE | NOT NULL | FK→ | The primary key to the interp_component table. An internal system-assigned number. On this table, it provides a link to the interp_component row for the result hash defined. |
| 13 | `INTERP_RANGE_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the interp_range table. An internal system-assigned number. On this table, it provides a link to the interp_range row. |
| 14 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the NOMENCLATURE table. An internal system-assigned number. On this table, it represents the medical nomenclature response for which the hash mark is defined. |
| 15 | `RESULT_CD` | DOUBLE | NOT NULL |  | Not currently used. |
| 16 | `RESULT_HASH` | VARCHAR(25) |  |  | The actual hash mark used to represent this result within the interpretation pattern (ex. "0", "1", "2", etc.) |
| 17 | `RESULT_HASH_ID` | DOUBLE | NOT NULL |  | The primary key of this table. An internal system-assigned number that ensure the uniqueness of each row. |
| 18 | `SEQUENCE` | DOUBLE |  |  | The sequence in which this assay's hash mark should be placed, in order to make up the interpretation pattern. |
| 19 | `TO_RESULT_RANGE` | DOUBLE |  |  | The highest number in the range of numeric results for which this hash mark applies. This column only applies to numeric results. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INCLUDED_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `INTERP_DETAIL_ID` | [INTERP_COMPONENT](INTERP_COMPONENT.md) | `INTERP_DETAIL_ID` |
| `INTERP_ID` | [INTERP_TASK_ASSAY](INTERP_TASK_ASSAY.md) | `INTERP_ID` |
| `INTERP_RANGE_ID` | [INTERP_RANGE](INTERP_RANGE.md) | `INTERP_RANGE_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

