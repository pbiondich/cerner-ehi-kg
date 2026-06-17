# CLINICAL_EVENT

> Stores patient related clinical information exclusively for clinical decision making. The information is part of the official medical record and discoverable. This information describes a point in time, not a duration. Individual rows can be a historical or current result or multiple rows can be connected to represent a larger structure (diagnostic documents, lab reports, medication administrations, etc.). See our structure diagrams for more information https://wiki.cerner.com/x/rIOSWQ

**Description:** clinical event  
**Table type:** ACTIVITY  
**Primary key:** `CLINICAL_EVENT_ID`  
**Columns:** 77  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_NBR` | VARCHAR(20) |  |  | Keyed (along with contributor_system). Allows access to events/groups of events via Accession Number. Scope and use of Accession Number is application-specific. |
| 2 | `AUTHENTIC_FLAG` | DOUBLE | NOT NULL |  | Determines whether the information stored in the event record has been authenticated. Valid values: 1 if event_status=authenticated, modified, or superseded; 0 for all others. |
| 3 | `CATALOG_CD` | DOUBLE | NOT NULL |  | Foreign key to the order_catalog table. Catalog_cd does not exist in the code_value table and does not have a code set.. |
| 4 | `CE_DYNAMIC_LABEL_ID` | DOUBLE | NOT NULL |  | The label_id of the dynamic label that this clinical event is associated with. (From CE_DYNAMIC_LABEL.label_id) |
| 5 | `CE_GROUPING_ID` | DOUBLE |  | FK→ | An identifier for grouping related clinical events to facilitate their display together. |
| 6 | `CE_GROUPING_TYPE_TFLG` | VARCHAR(30) |  |  | The Grouping type which is used to identify grouped clinical events. |
| 7 | `CE_GROUPING_VERSION_NBR` | DOUBLE |  |  | Version used to indicate that a particular event has been processed by the grouping service.; The service will add a value into the field as it processes items so it knows what rows have been processed. When the grouping service is updated, the version number will be increased so that the service can reprocess rows that have a lower value than the new version number.; |
| 8 | `CLINICAL_EVENT_ID` | DOUBLE | NOT NULL | PK | unique row identifier Unique identifier generated for each row of data in the clinical_event table. |
| 9 | `CLINICAL_SEQ` | VARCHAR(40) |  |  | This field describes the sequence of an event in a series. For example, 1,2,3 is one sequence or Post Op 1, Post Op2, Post Op3 could be another separate sequence. |
| 10 | `CLINSIG_UPDT_DT_TM` | DATETIME |  |  | Represents the update date/time that tracks when clinically significant updates are made to the Clinical Event and should only be used to check for updates. This field is used to notify audiences when a clinically significant update is made to an existing clinical event, such as when XR Clinical Reporting re-prints a lab result due to an update of the result value or when a result is resent to a provider's Message Center with the result update. This date should NOT be displayed as the clinically |
| 11 | `COLLATING_SEQ` | VARCHAR(40) |  |  | Used to define an ordering of sections within an MDOC. |
| 12 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 13 | `CRITICAL_HIGH` | VARCHAR(20) |  |  | Critical high value |
| 14 | `CRITICAL_LOW` | VARCHAR(20) |  |  | Critical low value. |
| 15 | `DEVICE_FREE_TXT` | VARCHAR(255) |  |  | A free text field that may be used to store the identifier for the device used to capture the event information. (Ex: IV Pump, Oral Fluid Pump, Ventilator, Glucometer) |
| 16 | `ENCNTR_FINANCIAL_ID` | DOUBLE | NOT NULL |  | The encounter financial id for the result |
| 17 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 18 | `ENTRY_MODE_CD` | DOUBLE | NOT NULL |  | Used to identify the method in which a result was entered. |
| 19 | `EVENT_CD` | DOUBLE | NOT NULL |  | It is the code that identifies the most basic unit of the storage, i.e. RBC, discharge summary, image. |
| 20 | `EVENT_CLASS_CD` | DOUBLE | NOT NULL |  | Coded value which specifies how the event is stored in and retrieved from the event table's sub-tables. For example, Event_Class_CDs identify events as numeric results, textual results, calculations, medications, etc. |
| 21 | `EVENT_END_DT_TM` | DATETIME | NOT NULL |  | Represents the clinically relevant date/time that is important to a clinical event. Should always be used as the date/time value for a result. It is the time the lab was drawn, or the temperature taken. Also referred to as the clinically relevant date, the service date, or the effective date. This date is intended to be displayed as the result date and used to qualify on the most recent result for a patient. The event_end_dt_tm is the field used in the Flowsheet if it is set to Clinical Range. |
| 22 | `EVENT_END_DT_TM_OS` | DOUBLE |  |  | If the event_end_dt_tm is precise, then this field is null. If the event_end_dt_tm is a "fuzzy" date, the event_end_dt_tm refers to the earliestdate/time that the event could have occurred, and the event_end_dt_tm_os is a fractional number of days representing the total range of fuzziness. |
| 23 | `EVENT_END_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 24 | `EVENT_ID` | DOUBLE | NOT NULL |  | Unique identifier for an event. Uniquely identifies a logical clinical event row. There may be more than one row with the same event_id, but only one of those rows will be current as indicated by the valid_until_dt_tm field. |
| 25 | `EVENT_RELTN_CD` | DOUBLE | NOT NULL |  | Relationship code: Parent, Child, Orphan |
| 26 | `EVENT_START_DT_TM` | DATETIME |  |  | Optional clinical date time for the start of the event. |
| 27 | `EVENT_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 28 | `EVENT_TAG` | VARCHAR(255) | NOT NULL |  | Brief text string to describe the event and to be displayed on the flowsheet. Calculated based on event class and status. |
| 29 | `EVENT_TAG_SET_FLAG` | DOUBLE |  |  | Event Tag Set Flag |
| 30 | `EVENT_TITLE_TEXT` | VARCHAR(255) |  |  | The title for document results. |
| 31 | `EXPIRATION_DT_TM` | DATETIME |  |  | The date on which the result no longer becomes clinically relevant. |
| 32 | `INQUIRE_SECURITY_CD` | DOUBLE | NOT NULL |  | Level of security required to view the content of the record. This is a denormalization for performance. |
| 33 | `MODIFIER_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | ID of Long Text row containing modifier text. Sequence: LONG_TEXT_SEQ |
| 34 | `NOMEN_STRING_FLAG` | DOUBLE | NOT NULL |  | Identifies which nomenclature table field will be used to calculate the event_tag. |
| 35 | `NORMALCY_CD` | DOUBLE | NOT NULL |  | States whether the result is normal. This can be used to determine whether to display the event tag in different color on the flowsheet. For group results, this represents an "overall" normalcy. i.e. Is any result in the group abnormal? Also allows different purge criteria to be applied based on result. |
| 36 | `NORMALCY_METHOD_CD` | DOUBLE | NOT NULL |  | The method used to interpret normalcy. |
| 37 | `NORMAL_HIGH` | VARCHAR(20) |  |  | Normal high value |
| 38 | `NORMAL_LOW` | VARCHAR(20) |  |  | Normal low value |
| 39 | `NORMAL_REF_RANGE_TXT` | VARCHAR(2000) |  |  | Stores normal reference text for results in which the normal cannot be defined using a numeric range supported by the NORMAL_LOW and NORMAL_HIGH fields. |
| 40 | `NOTE_IMPORTANCE_BIT_MAP` | DOUBLE |  |  | Contains bits for each note importance assigned to an attached note |
| 41 | `ORDER_ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | A sequence number used to identify the order of the actions. |
| 42 | `ORDER_ID` | DOUBLE | NOT NULL |  | Unique foreign key to Order Table. |
| 43 | `PARENT_EVENT_ID` | DOUBLE | NOT NULL |  | Provides a mechanism for logical grouping of events. i.e. supergroup and group tests. Same as event_id if current row is the highest level parent. |
| 44 | `PERFORMED_DT_TM` | DATETIME |  |  | Date this result was performed (or authored). |
| 45 | `PERFORMED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel id of provider who performed this result. |
| 46 | `PERFORMED_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 47 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 48 | `PUBLISH_FLAG` | DOUBLE | NOT NULL |  | States whether the item in this record is viewable via "normal" applications (e.g., charts, on-line inquiries, etc.). Audit and/or administrative applications would be able to view non-publishable results. |
| 49 | `QC_REVIEW_CD` | DOUBLE | NOT NULL |  | Result flagged for Review because value is outside review limits, or result was selected for QC review based on percentage or other selection algorithm. Values: no action, selected for review by limit exception, selected for review by algorithm, reviewed. There has not been a code set defined for this code yet. |
| 50 | `RECORD_STATUS_CD` | DOUBLE | NOT NULL |  | Record status code. Valid values: active, inactive, deleted combined away, needs review. |
| 51 | `REFERENCE_NBR` | VARCHAR(100) | NOT NULL |  | The combination of the reference nbr and the contributor system code provides a unique identifier to the origin of the data. |
| 52 | `RESOURCE_CD` | DOUBLE | NOT NULL |  | Service resource code for this event. |
| 53 | `RESOURCE_GROUP_CD` | DOUBLE | NOT NULL |  | Group service resource code for this event. |
| 54 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | Result status code. Valid values: authenticated, unauthenticated, unknown, cancelled, pending, in lab, active, modified, superseded, transcribed, not done. |
| 55 | `RESULT_TIME_UNITS_CD` | DOUBLE | NOT NULL |  | If the result refers to a rate, this field is the time component of the rate. |
| 56 | `RESULT_UNITS_CD` | DOUBLE | NOT NULL |  | The units of the result. |
| 57 | `RESULT_VAL` | VARCHAR(255) |  |  | The value of the result |
| 58 | `SERIES_REF_NBR` | VARCHAR(100) |  |  | Indicates a series of blobs; used to define the context within which replacement/succession of subsequent blobs can occur. |
| 59 | `SOURCE_CD` | DOUBLE | NOT NULL |  | Source from which a result value originated. For example the source can be father or mother or calculated etc. |
| 60 | `SRC_CLINSIG_UPDT_DT_TM` | DATETIME |  |  | The update date time of the source clinical event that is being copied to the target clinical event. |
| 61 | `SRC_EVENT_ID` | DOUBLE | NOT NULL |  | The event_id of the source clinical event that is being copied to the target clinical event. |
| 62 | `SUBTABLE_BIT_MAP` | DOUBLE |  |  | Each bit of this bit map is an indicator for existence of a row or a particular class of rows in a sub-table. |
| 63 | `SUBTABLE_BIT_MAP2` | DOUBLE |  |  | Extension of the SUBTABLE_BIT_MAP column; identifies the sub-tables that are associated with the event; |
| 64 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Foreign key to the discrete_task_assay table. Task_assay_cd does not exist in the code_value table and does not have a code set. |
| 65 | `TASK_ASSAY_VERSION_NBR` | DOUBLE |  |  | The version of the discrete task assay code. |
| 66 | `TRAIT_BIT_MAP` | DOUBLE |  |  | Represents traits about this clinical event, specifying types of information available for this event. |
| 67 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 68 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 69 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 70 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 71 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 72 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the Beginning Point of when a row in the table is valid. |
| 73 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the "End Point" of when a row in the table is valid. Current version of the result has an open 'Until Dt Tm" value. |
| 74 | `VERIFIED_DT_TM` | DATETIME |  |  | Date this result was verified. |
| 75 | `VERIFIED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel id of provider who verified this result. |
| 76 | `VERIFIED_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 77 | `VIEW_LEVEL` | DOUBLE | NOT NULL |  | Controls viewability of an Event row. Some rows are only used for grouping, etc. and should never be seen. Viewable results can vary depending on their importance. e.g., If the intellistrip is at the "Life" scale, only results which have meaning at the life granularity should appear. If the intellistrip is at the "Day" scale, then all results should be viewable. 0 = Not Viewable. 1 = Viewable at the lowest granularity of time. . . 9=Viewable at the highest granularity of time. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CE_GROUPING_ID` | [CLINICAL_EVENT](CLINICAL_EVENT.md) | `CLINICAL_EVENT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `MODIFIER_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PERFORMED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `VERIFIED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [CAC_DOCUMENT](CAC_DOCUMENT.md) | `CLINICAL_EVENT_ID` |
| [CLINICAL_EVENT](CLINICAL_EVENT.md) | `CE_GROUPING_ID` |
| [INFUSION_CE_RELTN](INFUSION_CE_RELTN.md) | `CLINICAL_EVENT_ID` |
| [SA_ANESTHESIA_RECORD](SA_ANESTHESIA_RECORD.md) | `CLINICAL_EVENT_ID` |
| [SA_DISPLAY_RESULT](SA_DISPLAY_RESULT.md) | `CLINICAL_EVENT_ID` |

