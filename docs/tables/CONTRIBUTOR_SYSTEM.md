# CONTRIBUTOR_SYSTEM

> The contributor system table contains information which controls the processing specific to each system that is sending transactions and data to be posted in Cerner system database.

**Description:** Contributor System  
**Table type:** REFERENCE  
**Primary key:** `CONTRIBUTOR_SYSTEM_CD`  
**Columns:** 47  
**Referenced by:** 12 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACT_CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Actual Contributor System Code ValueColumn |
| 6 | `ALT_CONTRIB_SRC_CD` | DOUBLE | NOT NULL |  | Specifies an alternate coding scheme of coded data used when performing code value alias translation for ESI and ESO transaction processing. Used only when the contributor source code does not find a match. |
| 7 | `AOF_ENABLED_IND` | DOUBLE | NOT NULL |  | When this field is active, the system states that code values will be added on the fly when possible. |
| 8 | `AUTHORIZATION_TYPE_CD` | DOUBLE | NOT NULL |  | The method used for the authorizing messages for this contributor system. |
| 9 | `AUTHORIZATION_URL` | VARCHAR(255) | NOT NULL |  | The URL for authorization information. |
| 10 | `AUTO_COMBINE_IND` | DOUBLE |  |  | When set on an authenticated feed, this logic will reconcile patients between the same or different contributor systems. It will reconcile all the records that meet the criteria set for "validate for authenticated combine" and "validate for unauthenticated combine" in the Reconcile tab of the ESI Configuration tool. |
| 11 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 12 | `CLIENT_IDENT` | VARCHAR(100) |  |  | Stores the clientId details to contributor_system table. ; Identifies the globally-unique identifier of the client application.; Values are of type UTF8(STRING). Values SHALL not exceed 100 characters in length. |
| 13 | `CONTRIBUTOR_SOURCE_CD` | DOUBLE | NOT NULL |  | Specifies the default coding scheme of coded data when performing code value alias translation for ESI and ESO transaction processing. |
| 14 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL | PK FK→ | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 15 | `CONTR_MODE_CD` | DOUBLE | NOT NULL |  | A description of the workflow that the contributor system is built for (ex: History, Batch, Real-time, etc). |
| 16 | `CONTR_SYS_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the contributor system is an AUTHENTICATED (more complete) or UNAUTHENTICATED (less complete) source of data for person and encounter information. |
| 17 | `DISPLAY` | VARCHAR(40) |  |  | DisplayColumn |
| 18 | `DOC_EVENT_CLASS_CD` | DOUBLE | NOT NULL |  | The event class code to use when the event_class_source_flag = 2 (Integrated departmental documents). |
| 19 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 20 | `ENHANCED_PROCESSING_CD` | DOUBLE | NOT NULL |  | Additonal processing occurs with this value is set. |
| 21 | `ESI_LOG_BITMAP` | DOUBLE | NOT NULL |  | This field defines the interaction between the ESI_LOG and LONG_BLOB tables for messages generated through the ESI Java server. |
| 22 | `ESI_ORG_ALIAS_CD` | DOUBLE | NOT NULL |  | Identifies the field in the HL7 transaction that contains the alias to the encounter organization. |
| 23 | `ESI_SPECIAL_SOURCE_FLAG` | DOUBLE | NOT NULL |  | Describes if and how a special coding system should be processed inbound. |
| 24 | `ESO_SPECIAL_SOURCE_FLAG` | DOUBLE | NOT NULL |  | Describes if and how a special coding system should be sent outbound. |
| 25 | `EVENT_CLASS_SOURCE_FLAG` | DOUBLE |  |  | Used for transcription interfaces to determine how to define the parent event class. The options are: Generic MDM documents (default), Generic and Departmental MDM documents, and Integrated Radiology MDM documents. |
| 26 | `GROUPER_HOLD_TIME` | DOUBLE | NOT NULL |  | An integer number of seconds to wait until releasing orders from the Grouper Server. Default value = 0. If greater than 0, this value will override the SCP release time on the ESI Server. |
| 27 | `GROUPER_MULTI_ORDS_IND` | DOUBLE | NOT NULL |  | Provides the ability to group orders without using timeframe or number of orders. With this option, an indicator must be sent in OBR-4 to notify the Grouper Server to release the orders for that encounter. |
| 28 | `IO_RESULT_IND` | DOUBLE | NOT NULL |  | Indicates whether the IO results from interface will be posted to CE_INTAKE_OUTPUT_RESULT table |
| 29 | `LISTENER_ALIAS` | VARCHAR(48) | NOT NULL |  | The selected Listener Alias is used for Outbound Document Processing through devices associated to this Contributor System |
| 30 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of facility. |
| 31 | `MAX_GROUPER_ORDERS` | DOUBLE | NOT NULL |  | The maximum integer number of orders to hold in the Grouper Server. Default value = 0. If greater than 0, this value will override the SCP release time on the ESI Server. |
| 32 | `MESSAGE_FORMAT_CD` | DOUBLE | NOT NULL |  | The format of the message, such as HL7, X12. |
| 33 | `MICRO_LIST_REPLACE_FLAG` | DOUBLE |  |  | For discrete microbiology results, determines how ESI will process updates to organisms and susceptibilities on the ce_susceptibility and/or ce_microbiology rows. The default will not do snapshot processing, but instead will update existing rows or add new rows. |
| 34 | `MICRO_MULTI_INTERP_IND` | DOUBLE |  |  | For discrete microbiology results, allows ESI to post multiple interps per antibiotic. |
| 35 | `OPF_MATCH_THRESHOLD` | VARCHAR(3) |  |  | Probabilistic matching weight required for contributor system to determine two people are duplicates and need to be auto combined |
| 36 | `OPF_REPORT_THRESHOLD` | VARCHAR(3) |  |  | Probabilistic matching weight required for contributor system to determine two people should show on the person matches report to be manually reviewed at a later time |
| 37 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Identifies the organization associated with the contributor system (feed). This value is the primary identifier of the organization table. |
| 38 | `PRSNL_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Personnel Person IDColumn |
| 39 | `RESULT_ALIAS_IND` | DOUBLE |  |  | Describes whether the alias will be used to find an orderable (as defined by order catalog) or event code alias. |
| 40 | `SYS_DIRECTION_CD` | DOUBLE | NOT NULL |  | Specifies the direction or usage of the contributor system. |
| 41 | `TIME_ZONE` | VARCHAR(100) |  |  | Default time zone to use for UTC processing if Time Zone Flag is set and no offsets are sent in the HL7 message. |
| 42 | `TIME_ZONE_FLAG` | DOUBLE |  |  | Determines if ESI will use time zone information from the contributor_system table or use offsets sent in the HL7 message to adjust the time for UTC or other time zone processing. |
| 43 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTRIBUTOR_SYSTEM_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRSNL_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (12)

| From table | Column |
|------------|--------|
| [DISPENSE_HX](DISPENSE_HX.md) | `CONTRIBUTOR_SYSTEM_CD` |
| [ESI_ALIAS_TRANS](ESI_ALIAS_TRANS.md) | `CONTRIBUTOR_SYSTEM_CD` |
| [ESI_ENSURE_PARMS](ESI_ENSURE_PARMS.md) | `CONTRIBUTOR_SYSTEM_CD` |
| [MATCH_TAG_PARMS](MATCH_TAG_PARMS.md) | `CONTRIBUTOR_SYSTEM_CD` |
| [ORG_CONTRIBUTOR_SYS_RELTN](ORG_CONTRIBUTOR_SYS_RELTN.md) | `CONTRIBUTOR_SYSTEM_CD` |
| [PERSON_PHR_RELTN](PERSON_PHR_RELTN.md) | `CONTRIBUTOR_SYSTEM_CD` |
| [PERSON_PHR_RELTN_HIST](PERSON_PHR_RELTN_HIST.md) | `CONTRIBUTOR_SYSTEM_CD` |
| [PFT_ENCNTR_COLLECTION_RELTN](PFT_ENCNTR_COLLECTION_RELTN.md) | `CONTRIBUTOR_SYSTEM_CD` |
| [SI_CONTRIBUTOR_SYSTEM_HIST](SI_CONTRIBUTOR_SYSTEM_HIST.md) | `CONTRIBUTOR_SYSTEM_CD` |
| [SI_CUSTOM_CDG_LOG](SI_CUSTOM_CDG_LOG.md) | `CONTRIBUTOR_SYSTEM_CD` |
| [SI_SPECIAL_CONFIG_OPTIONS](SI_SPECIAL_CONFIG_OPTIONS.md) | `CONTRIBUTOR_SYSTEM_CD` |
| [SI_XDOC_QUERY_PERSON_RELTN](SI_XDOC_QUERY_PERSON_RELTN.md) | `CONTRIBUTOR_SYSTEM_CD` |

