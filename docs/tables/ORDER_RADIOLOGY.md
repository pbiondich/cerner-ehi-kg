# ORDER_RADIOLOGY

> The Order_Radiology table contains radiology specific order information.

**Description:** Order Radiology  
**Table type:** ACTIVITY  
**Primary key:** `ORDER_ID`  
**Columns:** 51  
**Referenced by:** 20 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(20) |  |  | The Accession field contains the accession number that this order was assigned to at order time. |
| 2 | `ACCESSION_ID` | DOUBLE | NOT NULL | FK→ | The Accession_Id field is a foreign key to the Accession table. |
| 3 | `ACC_ADD_ON_IND` | DOUBLE | NOT NULL |  | This column indicates if the order was a part of an Accession Add-on transaction. |
| 4 | `CANCEL_BY_ID` | DOUBLE | NOT NULL | FK→ | If the order was cancelled the Cancel_By_Id contains the unique Identifier for the person who cancelled the order. |
| 5 | `CANCEL_DT_TM` | DATETIME |  |  | If the order was cancelled the Cancel_Dt_Tm contains the date and time that the order was cancelled. |
| 6 | `CANCEL_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 7 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The Catalog_Cd is a foreign key to the Order_Catalog table. This identifies which exam was ordered. |
| 8 | `COMMENTS` | VARCHAR(255) |  |  | The Comments field contains any general comments pertaining to the order. |
| 9 | `COMPLETE_DT_TM` | DATETIME |  |  | The Complete_Dt_Tm captures the date and time that the exam was performed. |
| 10 | `COMPLETE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 12 | `EXAM_AUTO_REPORT_IND` | DOUBLE |  |  | Indicates if the exam is auto-reported. |
| 13 | `EXAM_STATUS_CD` | DOUBLE | NOT NULL |  | The Exam_Status_Cd contains the current status of the exam portion of the order. |
| 14 | `GROUP_EVENT_ID` | DOUBLE | NOT NULL |  | The Group_Event_Id is a foreign key to the Clinical_Event table. |
| 15 | `GROUP_REFERENCE_NBR` | VARCHAR(40) |  |  | The Group_Reference_Nbr serves as a secondary tie to the Clinical_Event table. |
| 16 | `HIDE_PRELIM_REPORT_IND` | DOUBLE | NOT NULL |  | Indicates if the preliminary report is to be hidden from viewing outside RADNET. |
| 17 | `ORDER_ID` | DOUBLE | NOT NULL | PK FK→ | The Order_Id is a foreign key to the Orders table. It is used to uniquely identify an order. |
| 18 | `ORDER_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | The Order_Physician_Id contains the unique id of the physician who ordered the procedure. |
| 19 | `ORD_LOC_CD` | DOUBLE | NOT NULL |  | the Ord_Loc_Cd identifies the Location from which the order was placed. |
| 20 | `ORIG_ORDER_DT_TM` | DATETIME |  |  | The Original order date and time for this order. |
| 21 | `PACKET_ROUTING_CD` | DOUBLE | NOT NULL |  | The Packet_Routing_Cd identifies which packet routing to use for printing of the patient packet. This field is not always filled out. |
| 22 | `PARENT_ORDER_ID` | DOUBLE | NOT NULL | FK→ | The Parent_Order_Id is used during accession linking of a report. It contains the Order_Id of the master. This is only filled out after the report has been at least started. |
| 23 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 24 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | The Priority_Cd identifies the priority of the order. |
| 25 | `PROTOCOL_REQ_IND` | DOUBLE |  |  | Indicates a protocol is required for this exam. Null indicates the order existed prior to protocol functionality being available in Millennium. |
| 26 | `PULL_LIST_ID` | DOUBLE | NOT NULL | FK→ | The Pull_List_Id is a foreign key to the Pull_List table. It identifies which pull list is related to this order. |
| 27 | `RAD_PACS_ID` | DOUBLE | NOT NULL |  | This field is used as a unique identifier for PACS interfaces. |
| 28 | `REASON_FOR_EXAM` | VARCHAR(4000) |  |  | The Reason_For_Exam field contains a textual reason of why the procedure was performed. |
| 29 | `REFER_LOC_CD` | DOUBLE | NOT NULL |  | The Refer_Loc_Cd identifies where the order was referred from. |
| 30 | `REMOVED_BY_ID` | DOUBLE | NOT NULL | FK→ | If the order was removed after completion, the Removed_By_Id contains the Id of the person performing the remove. |
| 31 | `REMOVED_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 32 | `REMOVED_DT_TM` | DATETIME |  |  | If the order was removed after completion, the Removed_Cd Identifies why the exam was removed. |
| 33 | `REPLACED_ORDER_ID` | DOUBLE | NOT NULL | FK→ | This column, when valued, will reference the order that was cancelled as a part of a replace transaction. |
| 34 | `REPORTING_PRIORITY_CD` | DOUBLE | NOT NULL |  | This column contains the code value to allow for either ROUTINE or STAT priority. The STAT priority alerts the radiology tech to focus on first. |
| 35 | `REPORT_STATUS_CD` | DOUBLE | NOT NULL |  | The Report_Status_Cd identifies the current status of the report that a part of this order. |
| 36 | `REQUESTED_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 37 | `REQUEST_DT_TM` | DATETIME |  |  | The Request_Dt_Tm field contains the date and time that the order was requested to be performed. |
| 38 | `RESTORED_IND` | DOUBLE |  |  | The Restored_Ind indicates whether or not this order was restored from the repository for the purpose of changing the report. |
| 39 | `SEQ_EXAM_ID` | DOUBLE | NOT NULL | FK→ | The Seq_Exam_Id is a foreign key to the Exam_Data table. It serves as a link to the exam info within the exam management area. |
| 40 | `START_DT_TM` | DATETIME |  |  | The Start_Dt_tm contains the date and time that the exam was started. This is used for turnaround times. |
| 41 | `START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 42 | `TRANS_WORKGROUP_CD` | DOUBLE | NOT NULL |  | The Trans_Workgroup_Cd identifies the transcription workgroup that the report will be loaded to. |
| 43 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `VETTING_DT_TM` | DATETIME |  |  | This column will contain the date and time that the exam was vetted. |
| 49 | `VETTING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This column will contain the id of the personnel that vetted the exam. |
| 50 | `VETTING_STATUS_FLAG` | DOUBLE | NOT NULL |  | This is the vetting status of the exam.Valid values for this column are: 0 - Not Vetted; 1- Accepted; 2- Rejected; 3- Replaced; 4 - In Process |
| 51 | `VETTING_TZ` | DOUBLE |  |  | Time zone associated with the corresponding vetting_dt_tm column. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCESSION_ID` | [ACCESSION](ACCESSION.md) | `ACCESSION_ID` |
| `CANCEL_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORDER_PHYSICIAN_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PARENT_ORDER_ID` | [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PULL_LIST_ID` | [PULL_LIST](PULL_LIST.md) | `PULL_LIST_ID` |
| `REMOVED_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REPLACED_ORDER_ID` | [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `ORDER_ID` |
| `SEQ_EXAM_ID` | [EXAM_DATA](EXAM_DATA.md) | `SEQ_EXAM_ID` |
| `VETTING_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (20)

| From table | Column |
|------------|--------|
| [EXAM_CRITIQUE_INFO](EXAM_CRITIQUE_INFO.md) | `ORDER_ID` |
| [ICLASS_ACC_ORDER_R](ICLASS_ACC_ORDER_R.md) | `ORDER_ID` |
| [MAMMO_STUDY](MAMMO_STUDY.md) | `ORDER_ID` |
| [OMF_RADPROC_CLASS_ST](OMF_RADPROC_CLASS_ST.md) | `ORDER_ID` |
| [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `PARENT_ORDER_ID` |
| [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `REPLACED_ORDER_ID` |
| [PROC_CLASSIFICATION](PROC_CLASSIFICATION.md) | `ORDER_ID` |
| [PULL_ORD_SCHED](PULL_ORD_SCHED.md) | `ORDER_ID` |
| [RAD_ACR_CODES](RAD_ACR_CODES.md) | `ORDER_ID` |
| [RAD_CRITICAL_RESOLVE](RAD_CRITICAL_RESOLVE.md) | `ORDER_ID` |
| [RAD_DOSE_SCAN_ORDER_R](RAD_DOSE_SCAN_ORDER_R.md) | `ORDER_ID` |
| [RAD_EXAM](RAD_EXAM.md) | `ORDER_ID` |
| [RAD_FILM_ADJUST](RAD_FILM_ADJUST.md) | `ORDER_ID` |
| [RAD_INIT_READ](RAD_INIT_READ.md) | `ORDER_ID` |
| [RAD_PACKET](RAD_PACKET.md) | `ORDER_ID` |
| [RAD_PROTOCOL_ACT](RAD_PROTOCOL_ACT.md) | `ORDER_ID` |
| [RAD_PROTOCOL_ACT_HIST](RAD_PROTOCOL_ACT_HIST.md) | `ORDER_ID` |
| [RAD_REPORT](RAD_REPORT.md) | `ORDER_ID` |
| [RAD_RPT_LOCK](RAD_RPT_LOCK.md) | `ORDER_ID` |
| [RAD_VETTING_HOLD_DETAIL](RAD_VETTING_HOLD_DETAIL.md) | `ORDER_ID` |

