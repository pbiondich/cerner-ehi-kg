# LAB_INSTRUMENT

> Sub table to service resource containing resources which are instruments.

**Description:** Lab Instrument  
**Table type:** REFERENCE  
**Primary key:** `SERVICE_RESOURCE_CD`  
**Columns:** 64  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AUTHENTICATION_ID` | DOUBLE | NOT NULL |  | Identification of person authenticating MDI feed. This column is no longer used and should be considered OBSOLETE. The AUTH table is an obsolete table. |
| 3 | `AUTO_EXPLODE_IND` | DOUBLE |  |  | MDI flag which designates whether the order is automatically exploded or not. |
| 4 | `AUTO_VERIFY_FLAG` | DOUBLE |  |  | Not Used |
| 5 | `AV_CHECK_PART_QC_FLAG` | DOUBLE | NOT NULL |  | A value of 1 indicates that all QC for the run must be in control for autoverification to take place. A value of 2 indicates that if QC for an individual assay is out of control, assay processing for patient results will account for the QC when evaluating orderable parameters. A value of 3 indicates that if QC for an individual assay is out of control, assay processing for patient results will not account for the QC when evaluating orderable parameters and instead will only look at assays that |
| 6 | `AV_CHK_PART_QC_IND` | DOUBLE |  |  | A value of 0 indicates that if the run for QC is out for the instrument then no autoverify will take place. A value of 1 indicates that if the run for QC is out for the instrument then check the individual assay to see if the instrument is performing the assay okay. |
| 7 | `AV_FLAG` | DOUBLE |  |  | Determines how the results received from the instrument will automatically verify. |
| 8 | `AV_IND` | DOUBLE |  |  | A value of 0 means that autoverify is currently turned on for the instrument. A value of 1 means that autoverify is currently turned off for the instrument. |
| 9 | `AV_PART_IND` | DOUBLE |  |  | 0 : Orderable level autoverification with assay results received in single message1: Orderable level autoverification with assay results received in multiple messages |
| 10 | `AV_QC_IND` | DOUBLE |  |  | A value of 0 indicates that QC will not be autoverified if in control. A value of 1indicates that QC will be autoverifiedif in control. |
| 11 | `AV_QC_PART_IND` | DOUBLE |  |  | A value of 0 will not allow verification of QC results if any of the results are out of control. A value of 1 will allow verification of each QC result that is in control. |
| 12 | `AV_REQ_QC_IND` | DOUBLE |  |  | A value of 0 indicates that QC will not be checked before person results will be autoverified. A value of 1 indicates that QC will be checked before person results will be autoverified. |
| 13 | `CONTAINER_IND` | DOUBLE |  |  | The type of container for the instrument |
| 14 | `CQM_ALIAS_NAME` | VARCHAR(48) |  |  | The destination for inbound results. Applies to direct download and host query bidirectional interfaces. Similar to version 300's Transmit Queue (TQ) file. Used by the instrument interface team. |
| 15 | `CQM_APP_NAME` | VARCHAR(12) |  |  | The destination for inbound results. Applies to direct download and host query bidirectional interfaces. Similar to version 300's Transmit Queue (TQ) file. Used by the instrument interface team. |
| 16 | `CQM_CONTRIB_NAME` | VARCHAR(48) |  |  | Not currently being used as of March 1997 |
| 17 | `DISABLE_MICRO_PROBABILITY_IND` | DOUBLE | NOT NULL |  | Indicates that the Microbiology Instrument will not send the probability percentage to the instrument interface for organism identification. |
| 18 | `GATE_IND` | DOUBLE |  |  | For future use with gate indicator and gate codes. |
| 19 | `HOLIDAY_SCHEDULE_CD` | DOUBLE | NOT NULL |  | The holiday schedule associated with this instrument for autoverification & clinical validation. |
| 20 | `IDENTIFIER_FLAG` | DOUBLE |  |  | Identifies which type of identifier to use, e.g., accession no., tray/cup, sequence, etc. |
| 21 | `ID_MAP_JULIAN` | CHAR(18) |  |  | This field represents which digits of the full Julian accession number should be used when generating the Instrument Id Number. The value should consist of a string of 0's and 1's with the 1's representing the digits that should be used to generate the Id number. Example for Vitek: "000000000011001111" This will generate an Id number with the last two digits of the Julian date and the last four digits of the sequence number. |
| 22 | `ID_MAP_PREFIX` | CHAR(18) |  |  | This field represents which digits of the full prefixed accession number should be used when generating the Instrument Id Number. The value should consist of a string of 0's and 1's with the 1's representing the digits that should be used to generate the Id number. |
| 23 | `ID_NBR_SIZE` | CHAR(2) |  |  | This field represents the size of the Id number that should be generated based on the limitations of the instrument. This does NOT include the isolate number when determining the size. For Vitek the value should be "06". |
| 24 | `ID_TYPE` | CHAR(1) |  |  | This field represents whether the Id number should be numeric or alpha numeric based on the instrument limitations. For Vitek it should be "N". |
| 25 | `INSTRU_TYPE` | DOUBLE |  |  | Indicates how the interface should write the outbound download record when duplicate procedures within an order. There are there option for the instrument type. 1 = insert download records with lock trigger and update logic turned on. This is normally use for direct download 2 = Insert download records with lock trigger and no update turned on. This is normally use for direct download 3 = Insert tq with no trigger but with update logic turned on. This is normally used with host query |
| 26 | `INSTR_ALIAS` | VARCHAR(100) |  |  | Description of the instrument. User defined. |
| 27 | `INSTR_IDENTIFIER` | DOUBLE |  |  | For future use with multiplexor logic. |
| 28 | `INSTR_NAME` | VARCHAR(20) |  |  | For future use with multiplexor logic. |
| 29 | `INTFC_PROGNAME` | CHAR(15) |  |  | Contains the interface program name for the service resource. |
| 30 | `ISOLATE_NBR_SIZE` | CHAR(1) |  |  | This field represents the length of the isolate number. The isolate number will be appended to the end of the id number making the full id number that gets generated at susceptibility order time. For Vitek it should be "1". |
| 31 | `ISOLATE_TYPE` | CHAR(1) |  |  | This field represents how the isolate number should be generated. If it is set to "0" then the isolate number will match with the organism number that the susceptibility is being ordered on. If the susceptibility is ordered on Organism number 2 then the isolate number will be 2. If it is set to "1" then the isolate number will be set to the number of susceptibilities that have been ordered for that accession. It will increment by one with each susceptibility order on the accession. |
| 32 | `LOG_FLAG` | DOUBLE | NOT NULL |  | Controls log level journaling for MDI capture files |
| 33 | `MIC_AUTO_INTERP_FLAG` | DOUBLE |  |  | This field is used to determine if interpretations should automatically take place when results are sent back from the instrument. This field is currently not used. |
| 34 | `MIC_DOWNLOAD_LEVEL_FLAG` | DOUBLE |  |  | Not really sure what this field does, but will find out eventually from Dennis Boyer |
| 35 | `MIC_ID_PROB_LIMIT` | DOUBLE |  |  | This represents a percentage threshold that the user will set which determine whether organism name changes should occur. If the instrument sends a percent probability of the organism that is greater than or equal to the value in this field then an isolate name change will automatically occur. |
| 36 | `MIC_SEC_INTERP_IND` | DOUBLE |  |  | If this field is true then second level interps will be fired when results are received from the instrument. This field is currently not used. |
| 37 | `MULTIPLEXOR_ALIAS` | CHAR(20) |  |  | Identifies the name/code that a multiplexor sends back to MDI via the MDI interface. |
| 38 | `MULTIPLEXOR_IND` | DOUBLE |  |  | Used to identity if the instrument is a multiplexor. Is 1 if the instrument is a multiplexor, 0 if it is not. |
| 39 | `OPER_MODE` | CHAR(1) |  |  | Identifies interface functionality with regards to bidirectional, unidirectional or Host Query. B, U, or Q respectively. |
| 40 | `POINT_OF_CARE_FLAG` | DOUBLE |  |  | Indicates whether the instrument is at the point of patient care or whether it is located in a laboratory location. Filtering mechanism so the Point of Care applications will only display the appropriate instruments and not those in the lab. |
| 41 | `PRSNL_BEG_EFF_DT_TM` | DATETIME |  |  | to be removed June 1997 |
| 42 | `PRSNL_END_EFF_DT_TM` | DATETIME |  |  | to be removed June 1997 |
| 43 | `PRSNL_ID` | DOUBLE | NOT NULL |  | to be removed June 1997 |
| 44 | `RESULT_FORMAT_CD` | DOUBLE | NOT NULL |  | Identifies the format that will be used for packaging results. |
| 45 | `RMOD` | VARCHAR(20) |  |  | This stores the revision modification value of the related interface. The value is determined by the type of device. |
| 46 | `ROBOTICS_ALIQUOT_DIGIT` | CHAR(1) |  |  | Stores the aliquot digit to be appended to the accession for instruments associated to a robotics line. |
| 47 | `ROBOTICS_DEST` | DOUBLE |  |  | Identifies default destination route/analyzer. |
| 48 | `ROBOTICS_NAME` | VARCHAR(20) |  |  | Unique identifier for each analyzer connection to the robotics line. |
| 49 | `ROUTE_AT_COMPLETION_IND` | DOUBLE |  |  | Delays container routing to destination until tests are completed. |
| 50 | `SCHEDULE_CD` | DOUBLE | NOT NULL |  | The schedule associated with this instrument for autoverification and clinical validation. |
| 51 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | PK FK→ | The internal identifier for the instrument. |
| 52 | `STATION` | CHAR(4) |  |  | Defines the VMS logical that the interface will use to connect to the analyzer. |
| 53 | `STRT_MODEL_ID` | DOUBLE | NOT NULL | FK→ | The internal identifier for the instrument's Model. These model id's are a Cerner defined reference database |
| 54 | `UPDATE_REQUEST_NUMBER` | DOUBLE | NOT NULL |  | Request Number used by MDI Order Server to call a script which formats tests when doing updates. |
| 55 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 56 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 57 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 58 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 59 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 60 | `VERBOSITY` | CHAR(1) |  |  | Defines the level of journaling by the interface program to the capture files. Off, On, or Debug levels. |
| 61 | `VERIFY_BARCODE_IND` | DOUBLE |  |  | Enables automatic rerouting if barcodes are misread. |
| 62 | `WORKLIST_BUILD_FLAG` | DOUBLE |  |  | Indicates how worklists should be built. Valid values are Automatically, Manually, Not used. Functionality is not currently available as of March 1997 |
| 63 | `WORKLIST_HOURS` | DOUBLE |  |  | The maximum number of hours that a worklist is valid for accepting new accessions |
| 64 | `WORKLIST_MAX` | DOUBLE |  |  | The maximum number of accessions for a worklist. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `STRT_MODEL_ID` | [STRT_MODEL](STRT_MODEL.md) | `STRT_MODEL_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MDI_APPL_ACK](MDI_APPL_ACK.md) | `SERVICE_RESOURCE_CD` |

