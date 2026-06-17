# SUB_SECTION

> The Sub_Section table is a child of the service resource table and contains information specific to sub sections.

**Description:** Sub Section  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CQM_ALIAS_NAME` | CHAR(48) |  |  | The destination for inbound results. Applies to direct download and host query bidirectional interfaces. Similar to version 300's Transmit Queue (TQ) file. Used by the instrument interface team. |
| 2 | `CQM_APP_NAME` | CHAR(12) |  |  | The destination for inbound results. Applies to direct download and host query bidirectional interfaces. Similar to version 300's Transmit Queue (TQ) file. Used by the instrument interface team. |
| 3 | `ID_MAP_JULIAN` | CHAR(18) |  |  | This field represents which digits of the full Julian accession number should be used when generating the Instrument Id Number. The value should consist of a string of 0's and 1's with the 1's representing the digits that should be used to generate the Id number. Example for Vitek: "000000000011001111" This will generate an Id number with the last two digits of the Julian date and the last four digits of the sequence number. |
| 4 | `ID_MAP_PREFIX` | CHAR(18) |  |  | This field represents which digits of the full prefixed accession number should be used when generating the Instrument Id Number. The value should consist of a string of 0's and 1's with the 1's representing the digits that should be used to generate the Id number. |
| 5 | `ID_NBR_SIZE` | CHAR(2) |  |  | This field represents the size of the Id number that should be generated based on the limitations of the instrument. This does NOT include the isolate number when determining the size. For Vitek the value should be "06". |
| 6 | `ID_TYPE` | CHAR(1) |  |  | This field represents whether the Id number should be numeric or alpha numeric based on the instrument limitations. For Vitek it should be "N". |
| 7 | `INSTRU_TYPE` | DOUBLE |  |  | Indicates how the interface should write the outbound download record when duplicate procedures within an order. There are there option for the instrument type. 1 = insert download records with lock trigger and update logic turned on. This is normally use for direct download 2 = Insert download records with lock trigger and no update turned on. This is normally use for direct download 3 = Insert tq with no trigger but with update logic turned on. This is normally used with host query |
| 8 | `INSTR_ALIAS` | VARCHAR(100) |  |  | Description of the instrument. User defined. |
| 9 | `INSTR_NAME` | CHAR(20) |  |  | For future use with multiplexor logic. |
| 10 | `INTFC_PROGNAME` | CHAR(15) |  |  | Contains the interface program name for the service resource. |
| 11 | `ISOLATE_NBR_SIZE` | CHAR(1) |  |  | This field represents the length of the isolate number. The isolate number will be appended to the end of the id number making the full id number that gets generated at susceptibility order time. For Vitek it should be "1". |
| 12 | `ISOLATE_TYPE` | CHAR(1) |  |  | This field represents how the isolate number should be generated. If it is set to "0" then the isolate number will match with the organism number that the susceptibility is being ordered on. If the susceptibility is ordered on Organism number 2 then the isolate number will be 2. If it is set to "1" then the isolate number will be set to the number of susceptibilities that have been ordered for that accession. It will increment by one with each susceptibility order on the accession. |
| 13 | `MULTIPLEXOR_ALIAS` | CHAR(20) |  |  | Identifies the name/code that a multiplexor sends back to MDI via the MDI interface. |
| 14 | `MULTIPLEXOR_IND` | DOUBLE |  |  | Used to identity if the subsection is a multiplexor. Is 1 if the subsection is a multiplexor, 0 if it is not. |
| 15 | `OPER_MODE` | CHAR(1) |  |  | Identifies interface functionality with regards to bidirectional, unidirectional or Host Query. B, U, or Q respectively. |
| 16 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The Service_Resource_Cd is a foreign key to the Service_Resource table. It uniquely identifies a sub section. |
| 17 | `STATION` | CHAR(4) |  |  | Defines the VMS logical that the interface will use to connect to the analyzer. |
| 18 | `STRT_MODEL_ID` | DOUBLE |  |  | The internal identifier for the instrument's Model. These model id's are a Cerner defined reference database |
| 19 | `TRANSCRIPT_QUE_CD` | DOUBLE | NOT NULL | FK→ | Used by RadNet. The Transcipt_Que_Cd identifies the transcription workgroup that reports, within this sub section, will be queued to. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 25 | `VERBOSITY` | CHAR(1) |  |  | Defines the level of journaling by the interface program to the capture files. Off, On, or Debug levels. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `TRANSCRIPT_QUE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

